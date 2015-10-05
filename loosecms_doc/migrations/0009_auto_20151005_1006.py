# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import loosecms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0008_auto_20150930_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(help_text='Give the name of the document.', unique=True, max_length=200, verbose_name='title')),
                ('document_authors', models.TextField(verbose_name='document_authors', blank=True)),
                ('body', loosecms.fields.LoosecmsRichTextField(verbose_name='body')),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='loosecms_doc.Doc', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'loosecms_doc_doc_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'document Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='doctranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
