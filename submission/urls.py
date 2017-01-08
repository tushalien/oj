#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
app_name='submission'
urlpatterns = [
   # url(r'^$', views.submit_code, name='submit_code')
    url(r'^solve/(?P<pk>[a-zA-Z0-9]+)/$', views.solve, name='solve'),
    url(r'^solved/$', views.solved, name='solved'),
]