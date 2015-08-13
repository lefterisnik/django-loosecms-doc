# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import DocCategory, DocManager, Doc
from .plugin import DocPlugin


class DocAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', 'body')
    date_hierarchy = 'utime'
    list_display = ('title', 'manager', 'get_page', 'published')
    list_filter = ('manager__page', 'manager')
    list_editable = ('published',)

    def get_page(self, obj):
        return obj.manager.page
    get_page.short_description = _('Page')
    get_page.admin_order_field = 'manager__page'


class DocCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(DocCategory, DocCategoryAdmin)
admin.site.register(DocManager, DocPlugin)
admin.site.register(Doc, DocAdmin)