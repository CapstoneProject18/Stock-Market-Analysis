# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:31:08 2018

@author: GUL
"""
from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('details/', views.searching , name='details'),
    # url(r'^details/(?P<arg>[\w.@+\- \,\.]+)/$', views.details, name='details'),
    path('search/', views.details, name='search'),
];