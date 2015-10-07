# -*- coding: utf-8 -*-
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from ...models import Doc


class Command(BaseCommand):
    help = 'Move translations from one language to another in case of wrong input'

    def add_arguments(self, parser):
        parser.add_argument('language')
        parser.add_argument('-pk', '--doc-pk', type=int, dest='pk')
        parser.add_argument('-i', '--verbose', action='store_true', dest='verbose')

    def handle(self, *args, **options):
        language = options.get('language')
        verbose = options.get('verbose')
        pk = options.get('pk')

        DocTranslation = apps.get_model('loosecms_doc', 'DocTranslation')

        available_languages = [k for k, v in settings.LANGUAGES]
        if language not in available_languages:
            raise CommandError('Language not in LANGUAGES: %s' % language)

        # If pk is set, then get the article, else fetch all articles
        if pk:
            try:
                docs = Doc.objects.get(pk=pk)
                docs = [docs]
            except Doc.DoesNotExist:
                raise CommandError('Article "%s" does not exist' % pk)
        else:
            docs = Doc.objects.all()

        for doc in docs:
            # Fetch the translation of the article for the source language
            translation = self._get_translation(doc, DocTranslation, language)

            # If exists delete it
            if translation:
                translation.delete()

                if verbose:
                    self.stdout.write('Successfully delete translation for %s article' % doc.title)

            else:
                self.stdout.write('The %s article translation does not exist. Will continue to the next article.'
                                  % object.title)

        self.stdout.write('Successfully delete translations.')

    def _get_translation(self, object, DocTranslation, language):
        translations = DocTranslation.objects.filter(master_id=object.pk)
        try:
            # Try default translation
            return translations.get(language_code=language)
        except ObjectDoesNotExist:
            # Maybe the object was translated only in a specific language?
            # Hope there is a single translation
            return