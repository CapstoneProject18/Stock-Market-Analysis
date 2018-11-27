from __future__ import unicode_literals

try:
    from django.urls import path
except ImportError:
    from django.urls.defaults import path

from haystack.views import SearchView


urlpatterns = [
    path('', SearchView(), name='haystack_search'),
]
