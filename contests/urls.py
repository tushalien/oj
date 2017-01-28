#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
app_name = 'problem'
urlpatterns = [
     url(r'^$', views.home, name='home'),
     url(r'^add$', views.add, name='add'),
   
   

    ]