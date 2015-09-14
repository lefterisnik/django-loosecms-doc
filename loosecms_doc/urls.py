# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

from loosecms.views import detail

app_urlpatterns = [
    url(r'^download/(?P<pk>[0-9]+)/$', download, name='download-info'),
]

urlpatterns = [
    url(r'^doc-category/(?P<category_slug>[0-9A-Za-z-_.]+)/$', detail, name='doc-category-info')
]