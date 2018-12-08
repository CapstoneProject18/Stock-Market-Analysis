from django.urls import path
from . import views

urlpatterns = [
 	path(r'', views.fetch_compare, name='fetch'),
 	path(r'fetch/', views.fetch_compare, name='fetch_compare'),
 	path(r'company/', views.fetch_compare, name='company_compare')	
 ]