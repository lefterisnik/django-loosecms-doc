# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *
from .plugin import *

from parler.admin import TranslatableAdmin


class DocAdmin(TranslatableAdmin):
    search_fields = ('translations__title', 'translations__body')
    date_hierarchy = 'utime'
    list_display = ('title', 'manager', 'get_page', 'published')
    list_filter = ('manager__page', 'manager')
    list_editable = ('published',)
    fields = ('title', 'slug', 'document', 'document_authors', 'body', 'category', 'manager', 'login_required', 'published')


    def get_page(self, obj):
        return obj.manager.page

    get_page.short_description = _('Page')
    get_page.admin_order_field = 'manager__page'

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}


admin.site.register(Doc, DocAdmin)