# -*- coding:utf-8 -*-
from .models import DocManager, Doc
from loosecms.forms import PluginForm


class DocManagerForm(PluginForm):

    class Meta(PluginForm.Meta):
        model = DocManager