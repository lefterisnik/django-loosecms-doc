# -*- coding:utf-8 -*-
from .models import DocManager, NewsDocManager
from loosecms.forms import PluginForm


class DocManagerForm(PluginForm):

    class Meta(PluginForm.Meta):
        model = DocManager


class NewsDocManagerForm(PluginForm):

    class Meta(PluginForm.Meta):
        model = NewsDocManager