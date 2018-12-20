from django.conf.urls import url
from . import views

urlpatterns = [
 	url(r'', views.fetch_compare, name='fetch'),
 	url(r'fetch/', views.fetch_compare, name='fetch_compare'),
 	url(r'company/', views.fetch_compare, name='company_compare')	
 ]