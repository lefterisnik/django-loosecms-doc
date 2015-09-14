# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import loosecms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('loosecms_doc', '0003_auto_20150914_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='category',
            field=loosecms.fields.LoosecmsTaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='category'),
        ),
    ]
