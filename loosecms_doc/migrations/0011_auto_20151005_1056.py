# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0010_auto_20151005_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='body',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='document_authors',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='title',
        ),
    ]
