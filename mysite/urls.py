from django.conf.urls import url, include
from django.contrib import admin
from . import view
import re
from blog.views import MySearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
    url(r'^', include('comments.urls')),
]
