# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import Http404
from .models import Doc

import os, mimetypes


def download(request, pk):
        try:
            doc = Doc.objects.get(pk=pk)
        except Doc.DoesNotExist:
            raise Http404
        doc.update_hits()

        filename = os.path.basename(doc.document.path)
        mimetype, encoding = mimetypes.guess_type(filename)

        response = HttpResponse(content_type=mimetype)
        response['Content-Disposition'] = 'attachement; filename=%s' %filename.encode('utf-8')
        response.write(file(doc.document.path, 'rb').read())

        return response