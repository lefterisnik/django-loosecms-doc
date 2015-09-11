# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import loosecms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Give the name of the doc.', unique=True, max_length=200, verbose_name='title')),
                ('slug', models.SlugField(help_text='Give the slug of the doc. Is needed to create the url of rendering this article.', unique=True, verbose_name='slug')),
                ('document', loosecms.fields.UploadFilePathField(path=b'docs', verbose_name='document', recursive=True, upload_to=b'docs')),
                ('document_authors', models.TextField(verbose_name='document_authors', blank=True)),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('login_required', models.BooleanField(default=False, help_text='Check this box if login is required.', verbose_name='login required')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
                ('hits', models.IntegerField(default=0, editable=False)),
                ('published', models.BooleanField(default=True, verbose_name='published')),
            ],
        ),
        migrations.CreateModel(
            name='DocCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Give the name of the category.', unique=True, max_length=100, verbose_name='title')),
                ('slug', models.SlugField(help_text='Give the slug of the category. Is needed to create the url of rendering articles belong to this category.', unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='DocManager',
            fields=[
                ('plugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loosecms.Plugin')),
                ('title', models.CharField(help_text='Give the name of the doc manager.', max_length=200, verbose_name='title')),
                ('responsive', models.BooleanField(default=True, help_text='Check this box if you want the table to adapt to a very small screens under 768px.', verbose_name='responsive')),
                ('message', models.TextField(default='You will need to login in order to download this file', help_text='Give the message that will appear in the files that need a login user to download them.', verbose_name='message', blank=True)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(verbose_name='page', to='loosecms.HtmlPage', help_text='Select the page to render the doc manager. Additional, it used to create the urls of each article.')),
            ],
            bases=('loosecms.plugin',),
        ),
        migrations.CreateModel(
            name='NewsDocManager',
            fields=[
                ('plugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loosecms.Plugin')),
                ('title', models.CharField(help_text='Give the name of the doc news manager.', max_length=200, verbose_name='title')),
                ('number', models.IntegerField(help_text='Give the number of docs rendering by this manager', verbose_name='number')),
                ('header_title', models.CharField(default='Recent documents', help_text='Give the title of the panel which documents will appeared.', max_length=150, verbose_name='header title')),
                ('interval', models.PositiveSmallIntegerField(default=2000, help_text='Set the change rate in miliseconds.', verbose_name='interval')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(blank=True, to='loosecms_doc.DocManager', help_text='Select the document manager that contain the request documents. In case of no selection all documents form all managers will be included.', null=True, verbose_name='manager')),
            ],
            bases=('loosecms.plugin',),
        ),
        migrations.AddField(
            model_name='doc',
            name='category',
            field=models.ForeignKey(verbose_name='category', to='loosecms_doc.DocCategory', help_text='Select a category.'),
        ),
        migrations.AddField(
            model_name='doc',
            name='manager',
            field=models.ForeignKey(verbose_name='manager', to='loosecms_doc.DocManager', help_text='Select the doc manager.'),
        ),
    ]
