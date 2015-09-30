# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0007_auto_20150916_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsdocmanager',
            name='rss',
            field=models.BooleanField(default=False, help_text='Check this box if you want to appear the rss link in the header.', verbose_name='rss'),
        ),
        migrations.AddField(
            model_name='newsdocmanager',
            name='rss_description',
            field=models.CharField(help_text='Give a small description for the rss feed.', max_length=200, verbose_name='rss description', blank=True),
        ),
        migrations.AddField(
            model_name='newsdocmanager',
            name='rss_title',
            field=models.CharField(help_text='Give the title of the rss feed.', max_length=200, verbose_name='rss title', blank=True),
        ),
    ]
