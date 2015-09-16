# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify
from django.db import models, migrations

try:
    from unidecode import unidecode
except ImportError:
    unidecode = lambda slug: slug


def generate_slug_docmanager(apps, schema_editor):
    DocManager = apps.get_model('loosecms_doc', 'DocManager')
    for docmanager in DocManager.objects.all():
        docmanager.slug = slugify(unidecode(docmanager.title))
        docmanager.save()


def generate_slug_newsdocmanager(apps, schema_editor):
    NewsDocManager = apps.get_model('loosecms_doc', 'NewsDocManager')
    for newsdocmanager in NewsDocManager.objects.all():
        newsdocmanager.slug = slugify(unidecode(newsdocmanager.title))
        newsdocmanager.save()


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0005_auto_20150916_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='docmanager',
            name='slug',
            field=models.SlugField(help_text='Give the slug of the document manager.', verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='newsdocmanager',
            name='slug',
            field=models.SlugField(help_text='Give the slug of the document news manager.', verbose_name='slug'),
        ),
        migrations.RunPython(generate_slug_docmanager),
        migrations.RunPython(generate_slug_newsdocmanager),
    ]
