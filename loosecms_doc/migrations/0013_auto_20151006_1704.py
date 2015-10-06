# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0012_auto_20151006_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='docmanager',
            name='category_page',
            field=models.BooleanField(default=True, help_text='Check this box if you want to show all categories in this pageor show instant the table with the documents', verbose_name='show category page'),
        ),
        migrations.AddField(
            model_name='docmanager',
            name='hide_categories',
            field=models.BooleanField(default=False, help_text='Select if you want to hide the category list view.', verbose_name='hide categories list'),
        ),
    ]
