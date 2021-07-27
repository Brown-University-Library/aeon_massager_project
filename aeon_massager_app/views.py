import logging, pprint

from django.http import HttpResponse
from django.shortcuts import render

from urllib.parse import urlparse
# from django.urls import resolve


log = logging.getLogger(__name__)


def handler(request):
    log.debug( 'starting handler()' )
    # log.debug( f'request, ``{pprint.pformat(request.__dict__)}``' )
    log.debug( f'request.GET, ``{pprint.pformat(request.GET)}``' )

    log.debug( 'hereA' )

# https://docs.python.org/3.5/library/urllib.parse.html
# urllib.parse.parse_qs(
# urllib.parse.parse_qsl(

    return HttpResponse( 'handler response coming' )


def version(request):
    return HttpResponse( 'version response coming' )


def info(request):
    return HttpResponse( 'info response coming' )
