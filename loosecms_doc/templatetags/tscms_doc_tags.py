# -*- coding: utf-8 -*-
from django import template
import os

register = template.Library()

@register.filter
def filesize(value):
    '''
    Return the size of unicoded filepath
    '''
    filepath = value.document.path
    return os.stat(filepath.encode('utf-8')).st_size