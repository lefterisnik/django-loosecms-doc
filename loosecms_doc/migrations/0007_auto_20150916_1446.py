# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0006_auto_20150916_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docmanager',
            name='slug',
            field=models.SlugField(help_text='Give the slug of the document manager.', unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='newsdocmanager',
            name='slug',
            field=models.SlugField(help_text='Give the slug of the document news manager.', unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='slug',
            field=models.SlugField(help_text='Give the slug of the document. Is needed to create the url of rendering this document.', unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='title',
            field=models.CharField(help_text='Give the name of the document.', unique=True, max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='docmanager',
            name='title',
            field=models.CharField(help_text='Give the name of the document manager.', unique=True, max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='newsdocmanager',
            name='title',
            field=models.CharField(help_text='Give the name of the document news manager.', unique=True, max_length=200, verbose_name='title'),
        ),
    ]
