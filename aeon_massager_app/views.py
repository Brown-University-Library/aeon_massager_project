import logging, pprint

import django
from django.conf import settings as project_settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# from urllib.parse import urlparse
# from django.urls import resolve


log = logging.getLogger(__name__)


def handler(request):
    log.debug( 'starting handler()' )
    # log.debug( f'request, ``{pprint.pformat(request.__dict__)}``' )
    log.debug( f'request.GET, ``{pprint.pformat(request.GET)}``' )
    # params = {
    #     'action': request.GET.get( 'Action', '10' )
    # }
    # log.debug( f'params, ``{pprint.pformat(params)}``' )

    # param_dct = dict( request.GET )
    # log.debug( f'type(param_dct, ``{type(param_dct)}``' )
    # log.debug( f'param_dct, ``{pprint.pformat(param_dct)}``' )

    params_query_dict_copy = request.GET.copy()  # <https://stackoverflow.com/questions/5036498/django-rebuild-a-query-string-without-one-of-the-variables>
    assert type(params_query_dict_copy) == django.http.request.QueryDict, type(params_query_dict_copy)
    log.debug( f'params_query_dict_copy initially, ``{pprint.pformat(params_query_dict_copy)}``' )
    truncated_title = ''
    if 'ItemTitle' in params_query_dict_copy.keys():
        title = params_query_dict_copy['ItemTitle']
        if len( title ) > project_settings.TRUNCATE_LENGTH:
            len_minus_elipsis = project_settings.TRUNCATE_LENGTH - 3
            truncated_title = f'{title[0:len_minus_elipsis]}...'
            params_query_dict_copy['ItemTitle'] = truncated_title
    log.debug( f'params_query_dict_copy now, ``{pprint.pformat(params_query_dict_copy)}``' )
    encoded_qd = params_query_dict_copy.urlencode()
    assert type(encoded_qd) == str, type(encoded_qd)
    log.debug( f'encoded_qd, ``{encoded_qd}``' )


    # return HttpResponse( 'test' )

    redirect_url = f'https://jcbl.aeon.atlas-sys.com/aeon.dll?{encoded_qd}'
    return HttpResponseRedirect( redirect_url )



# Action=10&
# Form=30&
# ReferenceNumber={mms_id}&
# ItemTitle={rft.btitle}&
# ItemAuthor={rft.au}&
# ItemPublisher={rft.place}+{rft.publisher}&
# CallNumber={call_number}


    return HttpResponse( 'handler response coming' )


def version(request):
    return HttpResponse( 'version response coming' )


def info(request):
    return HttpResponse( 'info response coming' )
