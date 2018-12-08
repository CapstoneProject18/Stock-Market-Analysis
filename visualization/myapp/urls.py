from django.urls import path
from . import views

urlpatterns = [
 	path('', views.chart, name='chart'),
 	path('fetch/', views.fetch, name='fetch'),
 	path('company/', views.fetch, name='company')	
 ]