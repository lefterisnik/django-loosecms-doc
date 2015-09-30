# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

from loosecms.views import detail

urlpatterns = [
    url(r'^documents/syndication/(?P<manager_pk>[0-9]+)/$', NewsFeed(), name='document-syndication'),
]

embed_urlpatterns = [
    url(r'^(?P<slug>[0-9A-Za-z-_.]+)/$', detail, name='info'),
    url(r'^doc-category/(?P<category_slug>[0-9A-Za-z-_.]+)/$', detail, name='doc-category-info'),
    url(r'^download/(?P<pk>[0-9]+)/$', download, name='download-info'),
]