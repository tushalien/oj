#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
app_name = 'problem'
urlpatterns = [
     url(r'^listproblems/$', views.list, name='list'),
    # url(r'^$', views.edit_p, name='edit_p'),
     url(r'^solve/(?P<pk>[a-zA-Z0-9]+)/$', views.solve, name='solve'),
   

    ]