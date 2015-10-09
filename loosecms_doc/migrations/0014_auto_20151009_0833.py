# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import loosecms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0013_auto_20151006_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='category',
            field=loosecms.fields.LoosecmsTaggableManager(to='loosecms.LoosecmsTag', through='loosecms.LoosecmsTagged', blank=True, help_text='A comma-separated list of tags.', verbose_name='category'),
        ),
    ]
