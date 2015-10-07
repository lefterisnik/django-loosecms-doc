# -*- coding: utf-8 -*-
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from ...models import Doc


class Command(BaseCommand):
    help = 'Move translations from one language to another in case of wrong input'

    def add_arguments(self, parser):
        parser.add_argument('source')
        parser.add_argument('destination')
        parser.add_argument('-pk', '--doc-pk', type=int, dest='pk')
        parser.add_argument('-ds', '--delete-source', action='store_true', dest='ds')
        parser.add_argument('-i', '--verbose', action='store_true', dest='verbose')
        parser.add_argument('-ov', '--override', action='store_true', dest='override')

    def handle(self, *args, **options):
        source = options.get('source')
        destination = options.get('destination')
        verbose = options.get('verbose')
        override = options.get('override')
        pk = options.get('pk')
        ds = options.get('ds')

        DocTranslation = apps.get_model('loosecms_doc', 'DocTranslation')

        available_languages = [k for k, v in settings.LANGUAGES]
        if source not in available_languages:
            raise CommandError('Source language not in LANGUAGES: %s' % source)

        if destination not in available_languages:
            raise CommandError('Destination language not in LANGUAGES: %s' % source)

        # If pk is set, then get the article, else fetch all articles
        if pk:
            try:
                docs = Doc.objects.get(pk=pk)
                docs = [docs]
            except Doc.DoesNotExist:
                raise CommandError('Doc "%s" does not exist' % pk)
        else:
            docs = Doc.objects.all()

        for doc in docs:
            # Fetch the translation of the article for the source language
            source_doc = self._get_translation(doc, DocTranslation, source)

            # If exists, fetch translation of the article for the destination language (if exists set the new values
            # if not exists create an entry and set the values), else throw message
            if source_doc:
                destination_doc = self._get_translation(doc, DocTranslation, destination)
                if not destination_doc:
                    tmp_title, tmp_document_authors, tmp_body = source_doc.title, \
                                                                source_doc.document_authors, source_doc.body

                    # Because some values are unique we must delete first the source translation
                    source_doc.delete()

                    DocTranslation.objects.create(
                        master_id=doc.pk,
                        language_code=destination,
                        title=tmp_title,
                        document_authors=tmp_document_authors,
                        body=tmp_body
                    )
                else:
                    if override:
                        destination_doc.title = source_doc.title
                        destination_doc.document_authors = source_doc.document_authors
                        destination_doc.body = source_doc.body
                    else:
                        if not destination_doc.title:
                            destination_doc.title = source_doc.title
                        if not destination_doc.body:
                            destination_doc.body = source_doc.body
                        if not destination_doc.document_authors:
                            destination_doc.document_authors = source_doc.document_authors

                    # Because some values are unique we must delete first the source translation
                    source_doc.delete()

                    destination_doc.opened = False
                    destination_doc.save()

                    if verbose:
                        self.stdout.write('Successfully translation moving "new title: %s"' %
                                      (destination_doc.title))
                        self.stdout.write('Successfully translation moving "new body: %s"' %
                                      (destination_doc.body))
                        self.stdout.write('Successfully translation moving "new document authors: %s"' %
                                      (destination_doc.document_authors))
            else:
                self.stdout.write('The %s article translation does not exist. Will continue to the next article.'
                                  % object.title)

        self.stdout.write('Successfully translation moving.')

    def _get_translation(self, object, DocTranslation, language):
        translations = DocTranslation.objects.filter(master_id=object.pk)
        try:
            # Try default translation
            return translations.get(language_code=language)
        except ObjectDoesNotExist:
            # Maybe the object was translated only in a specific language?
            # Hope there is a single translation
            return