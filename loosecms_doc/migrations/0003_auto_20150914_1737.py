# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0002_auto_20150913_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='category',
        ),
        migrations.DeleteModel(
            name='DocCategory',
        ),
    ]
