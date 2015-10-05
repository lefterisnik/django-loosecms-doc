# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations
from django.core.exceptions import ObjectDoesNotExist


def forwards_func(apps, schema_editor):
    Doc = apps.get_model('loosecms_doc', 'Doc')
    DocTranslation = apps.get_model('loosecms_doc', 'DocTranslation')

    for object in Doc.objects.all():
        DocTranslation.objects.create(
            master_id=object.pk,
            language_code=settings.LANGUAGE_CODE,
            title=object.title,
            document_authors=object.document_authors,
            body=object.body
        )

def backwards_func(apps, schema_editor):
    Doc = apps.get_model('loosecms_doc', 'Doc')
    DocTranslation = apps.get_model('loosecms_doc', 'DocTranslation')

    for object in Doc.objects.all():
        translation = _get_translation(object, DocTranslation)
        object.title = translation.title
        object.document_authors = translation.document_authors
        object.body = translation.body
        object.save()   # Note this only calls Model.save() in South.

def _get_translation(object, DocTranslation):
    translations = DocTranslation.objects.filter(master_id=object.pk)
    try:
        # Try default translation
        return translations.get(language_code=settings.LANGUAGE_CODE)
    except ObjectDoesNotExist:
        try:
            # Try default language
            return translations.get(language_code=settings.PARLER_DEFAULT_LANGUAGE_CODE)
        except ObjectDoesNotExist:
            # Maybe the object was translated only in a specific language?
            # Hope there is a single translation
            return translations.get()


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms_doc', '0009_auto_20151005_1006'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]
