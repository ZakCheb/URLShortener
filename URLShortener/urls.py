from django.contrib import admin
from django.urls import path,re_path
from Shortener.views import *
from .settings import SHORT_URL_LENGHT

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^go/(?P<target>[a-zA-Z0-9]{{{}}})/$'.format(SHORT_URL_LENGHT),RedirectPage),
    
    path('',HomePage),
]
