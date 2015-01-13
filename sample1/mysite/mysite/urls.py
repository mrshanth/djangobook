from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *


urlpatterns = patterns('',
    url(r'^blah/$', blah),
    url(r'^hello/$', hello),
    url(r'^timenow/$', timenow),
    url(r'^timecal/(\d{1,2})/$', time_calc),
)
