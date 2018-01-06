from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
import requests


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def baidu_push(self):
        url = 'http://data.zz.baidu.com/urls?site=xxccxcxc.top&token=oE6j072TMctOd1lt'
        headers = {
            'Content-Type': 'text/plain'
        }
        url_list = []
        url_list.append('http://xxccxcxc.top/post/{}/'.format(self.pk))
        data = '\n'.join(url_list)
        requests.post(url, headers=headers, data=data)

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extension=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save(*args, **kwargs)
        self.baidu_push()

    class Meta:
        ordering = ['-created_time']

