# -*- coding: utf-8 -*-
from django.http import Http404
from django.contrib import admin
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from taggit.models import Tag

from .models import *

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin


class DocInline(admin.StackedInline):
    model = Doc
    extra = 1
    prepopulated_fields = {'slug': ('title', )}


class DocManagerPlugin(PluginModelAdmin):
    model = DocManager
    name = _('Document Container')
    plugin = True
    template = "plugin/docs.html"
    inlines = [
        DocInline,
    ]

    def update_context(self, context, manager):
        categories = Tag.objects.filter(doc__manager=manager).annotate(doc_count=Count('doc'))
        if 'kwargs' in context:
            if 'slug' in context['kwargs']:
                context['slug'] = context['kwargs']['slug']
                '''Fetch specific doc'''
                try:
                    docs = Doc.objects.select_related()\
                        .get(published=True, slug=context['slug'], manager=manager)
                except Doc.DoesNotExist:
                    raise Http404
            elif 'category_slug' in context['kwargs']:
                context['category_slug'] = context['kwargs']['category_slug']

                '''Fetch all docs for requested category'''
                docs = Doc.objects.select_related()\
                    .filter(published=True, category__slug=context['kwargs']['category_slug'], manager=manager)\
                    .order_by('-ctime')
                if len(docs) == 0:
                    raise Http404

        elif context['page_slug'] != '':
            ''' Fetch all articles for requested page'''
            docs = Doc.objects.select_related()\
                .filter(published=True, manager=manager)\
                .order_by('-ctime')

        context['docs'] = docs
        context['categories'] = categories
        context['docmanager'] = manager
        return context


class NewsDocManagerPlugin(PluginModelAdmin):
    model = NewsDocManager
    name = _('Recent Document Container')
    plugin = True
    template = "plugin/new_docs.html"
    fieldsets = (
        (None, {
            'fields': ('type', 'placeholder', 'title', 'number', 'published')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('manager', 'header_title', 'interval')
        }),
        ('Rss options', {
            'classes': ('collapse',),
            'fields': ('rss', 'rss_title', 'rss_description')
        }),
    )

    def update_context(self, context, manager):
        if manager.manager:
            newsdocs = Doc.objects.select_related().\
                               filter(published=True, manager=manager.manager).\
                               order_by('-ctime')[:manager.number]
        else:
            newsdocs= Doc.objects.select_related().\
                               filter(published=True).\
                               order_by('-ctime')[:manager.number]

        context['newsdocs'] = newsdocs
        context['newsdocmanager'] = manager
        return context

plugin_pool.register_plugin(DocManagerPlugin)
plugin_pool.register_plugin(NewsDocManagerPlugin)