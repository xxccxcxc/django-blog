from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>\d+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>\d+)/$', views.TagView.as_view(), name='tag'),
    # url(r'^search/', include('haystack.urls')),
    url(r'^search/', views.MySearchView(), name='haystack_search'),
]