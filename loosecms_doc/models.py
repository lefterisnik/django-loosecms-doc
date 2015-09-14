# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from loosecms.models import Plugin, HtmlPage
from loosecms.fields import UploadFilePathField, LoosecmsRichTextField, LoosecmsTaggableManager


class DocManager(Plugin):
    default_type = 'DocManagerPlugin'

    title = models.CharField(_('title'), max_length=200,
                             help_text=_('Give the name of the doc manager.'))
    page = models.ForeignKey(HtmlPage, verbose_name=_('page'),
                             limit_choices_to={'is_template': False},
                             help_text=_('Select the page to render the doc manager. Additional, it used to create the '
                                         'urls of each article.'))
    responsive = models.BooleanField(_('responsive'), default=True,
                                     help_text=_('Check this box if you want the table to adapt to a very small '
                                                 'screens under 768px.'))
    message = models.TextField(_('message'), blank=True,
                               default=_('You will need to login in order to download this file'),
                               help_text=_('Give the message that will appear in the files that need a login user '
                                           'to download them.'))
    ctime = models.DateTimeField(auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)


# TODO: Copy login from article
class NewsDocManager(Plugin):
    default_type = 'NewsDocManagerPlugin'

    title = models.CharField(_('title'), max_length=200,
                             help_text=_('Give the name of the doc news manager.'))
    number = models.IntegerField(_('number'),
                                 help_text=_('Give the number of docs rendering by this manager'))
    header_title = models.CharField(_('header title'), max_length=150,
                                    default=_('Recent documents'),
                                    help_text=_('Give the title of the panel which documents will appeared.'))
    manager = models.ForeignKey(DocManager, verbose_name=_('manager'), blank=True, null=True,
                                limit_choices_to={'published': True},
                                help_text=_('Select the document manager that contain the request documents. In case'
                                            ' of no selection all documents form all managers will be included.'))
    interval = models.PositiveSmallIntegerField(_('interval'), default=2000,
                                                help_text=_('Set the change rate in miliseconds.'))
    ctime = models.DateTimeField(auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)


class Doc(models.Model):
    title = models.CharField(_('title'), max_length=200, unique=True,
                             help_text=_('Give the name of the doc.'))
    slug = models.SlugField(_('slug'), unique=True,
                            help_text=_('Give the slug of the doc. Is needed to create the url of rendering this '
                                        'article.'))
    document = UploadFilePathField(_('document'), upload_to='docs', path='docs', recursive=True)

    document_authors = models.TextField(_('document_authors'), blank=True)

    body = LoosecmsRichTextField(_('body'))

    category = LoosecmsTaggableManager(_('category'))

    manager = models.ForeignKey(DocManager, verbose_name=_('manager'),
                                help_text=_('Select the doc manager.'))
    login_required = models.BooleanField(_('login required'), default=False,
                                         help_text=_('Check this box if login is required.'))
    ctime = models.DateTimeField(auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    hits = models.IntegerField(default=0, editable=False)

    published = models.BooleanField(_('published'), default=True)

    def update_hits(self):
        self.hits += 1
        self.save()

    def __unicode__(self):
        return self.title