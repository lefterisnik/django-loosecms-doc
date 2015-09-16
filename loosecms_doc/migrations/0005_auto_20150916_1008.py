# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0004_doc_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doc',
            options={'verbose_name': 'document', 'verbose_name_plural': 'documents'},
        ),
    ]
