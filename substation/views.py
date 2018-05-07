from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView
from django.utils.text import slugify
import markdown
from markdown.extensions.toc import TocExtension
import pygments
import requests
import json

class IndexView(ListView):
    model = Post
    template_name = 'substation/index.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        context['title'] = '首页'
        hitokoto = self.get_hitokoto()
        context.update(hitokoto)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        left = []
        right = []
        left_has_more = right_has_more = first = last = False
        lr_cnt = 2
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number > 1:
            left = page_range[(page_number - lr_cnt - 1) if (page_number - lr_cnt - 1) > 0 else 0:page_number - 1]
            left_has_more = (left[0] > 2)
            first = (left[0] > 1)
        if page_number < total_pages:
            right = page_range[page_number:page_number + lr_cnt]
            right_has_more = (right[-1] < total_pages - 1)
            last = (right[-1] < total_pages)
        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }
        return data

    def get_hitokoto(self):
        response = requests.get('https://sslapi.hitokoto.cn/?c=a')
        dict = json.loads(response.text)
        hitokoto = {
            'hitokoto': dict['hitokoto'],
            'from': dict['from'],
        }
        return hitokoto


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['title'] = '{} - 分类'.format(get_object_or_404(Category, pk=self.kwargs.get('pk')).name)
        return context


class ArchivesView(IndexView):
    def get_queryset(self):
        return super(ArchivesView, self).get_queryset().filter(created_time__year=self.kwargs.get('year'),
                                             created_time__month=self.kwargs.get('month'))

    def get_context_data(self, **kwargs):
        context = super(ArchivesView, self).get_context_data(**kwargs)
        context['title'] = '{} 年 {} 月 - 归档'.format(self.kwargs.get('year'), self.kwargs.get('month'))
        return context


class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['title'] = '{} - 标签'.format(get_object_or_404(Tag, pk=self.kwargs.get('pk')).name)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'substation/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        return response

    def get_object(self):
        post = super(PostDetailView, self).get_object()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            TocExtension(slugify=slugify)
        ])
        post.body = md.convert(post.body)
        post.toc = md.toc
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        hitokoto = self.get_hitokoto()
        context.update(hitokoto)
        return context


    def get_hitokoto(self):
        response = requests.get('https://sslapi.hitokoto.cn/?c=a')
        dict = json.loads(response.text)
        hitokoto = {
            'hitokoto': dict['hitokoto'],
            'from': dict['from'],
        }
        return hitokoto

