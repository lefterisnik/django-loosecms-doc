# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

app_urlpatterns = [
    url(r'^download/(?P<pk>[0-9]+)/$', download, name='download-info'),
]

urlpatterns = []