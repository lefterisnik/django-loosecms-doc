# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import loosecms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='body',
            field=loosecms.fields.LoosecmsRichTextField(verbose_name='body'),
        ),
    ]
