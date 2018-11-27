from django.urls import include, path
from django.contrib import admin
urlpatterns = [
    # Examples:
    # url(r'^$', 'testhystack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('search/', include('haystack.urls')),
    path('admin/', admin.site.urls),
]
