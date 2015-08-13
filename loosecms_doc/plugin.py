# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.template import loader
from django.contrib import admin
from django.http import Http404
from django.db.models import Count

from .forms import DocManagerForm
from .models import DocManager, Doc, DocCategory

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin


class DocInline(admin.StackedInline):
    model = Doc
    extra = 1
    prepopulated_fields = {'slug': ('title', )}


class DocPlugin(PluginModelAdmin):
    model = DocManager
    name = _('Documents')
    form = DocManagerForm
    plugin = True
    template = "plugin/doc.html"
    inlines = [
        DocInline,
    ]
    extra_initial_help = None
    fields = ('type', 'placeholder', 'title', 'page', 'responsive', 'message', 'published')

    def render(self, context, manager):
        categories = DocCategory.objects.annotate(Count('doc'))
        if 'kwargs' in context:
            if 'slug' in context['kwargs']:
                context['slug'] = context['kwargs']['slug']
                context['category_slug'] = context['kwargs']['category_slug']
                '''Fetch specific doc'''
                try:
                    docs = Doc.objects.select_related().get(published=True, slug=context['slug'])
                except Doc.DoesNotExist:
                    raise Http404
            elif 'category_slug' in context['kwargs']:
                context['category_slug'] = context['kwargs']['category_slug']

                '''Fetch all docs for requested category'''
                docs = Doc.objects.select_related().filter(published=True, category__slug=context['kwargs']['category_slug']).order_by('-ctime')
                if len(docs) == 0:
                    raise Http404

        elif context['page_slug'] != '':
            ''' Fetch all articles for requested page'''
            docs = Doc.objects.select_related().filter(published=True, manager=manager).order_by('-ctime')

        t = loader.get_template(self.template)
        context['docs'] = docs
        context['categories'] = categories
        context['docmanager'] = manager
        return t.render(context)

    def get_changeform_initial_data(self, request):
        initial = {}
        if self.extra_initial_help:
            initial['type'] = self.extra_initial_help['type']
            initial['placeholder'] = self.extra_initial_help['placeholder']
            initial['page'] = self.extra_initial_help['page']

            return initial
        else:
            return {'type': 'DocPlugin'}

plugin_pool.register_plugin(DocPlugin)