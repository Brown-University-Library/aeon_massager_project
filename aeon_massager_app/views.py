from django.http import HttpResponse
from django.shortcuts import render


def info(request):
    # return HttpResponse("Hello, world. You're at the info-I page.")
    resp = render( request, 'info.html', {'foo': 'DD'} )
    return resp
