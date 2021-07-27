from aeon_massager_app import views
from django.urls import path


urlpatterns = [
    ## main path
    path('handler/', views.handler, name='handler_url'),
    ## helper paths
    path('info/', views.info, name='info_url'),
    path('version/', views.version, name='version_url'),
]
