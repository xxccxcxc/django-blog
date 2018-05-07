from django.conf.urls import url
from . import views

app_name = 'substation'
urlpatterns = [
    url(r'^substation$', views.IndexView.as_view(), name='index'),
    url(r'^substation/post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^substation/archives/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^substation/category/(?P<pk>\d+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^substation/tag/(?P<pk>\d+)/$', views.TagView.as_view(), name='tag'),
    # url(r'^search/', include('haystack.urls')),
]