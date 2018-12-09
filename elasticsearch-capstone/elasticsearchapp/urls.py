# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:31:08 2018

@author: GUL
"""
from . import views
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^details/$', views.searching),
    # url(r'^details/(?P<arg>[\w.@+\- \,\.]+)/$', views.details, name='details'),
    url(r'^search/', views.details, name='search'),

];