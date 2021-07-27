from django.http import HttpResponse
from django.shortcuts import render


def handler(request):
    return HttpResponse( 'handler response coming' )


def version(request):
    return HttpResponse( 'version response coming' )


def info(request):
    return HttpResponse( 'info response coming' )
