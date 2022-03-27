from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('sw.js', RedirectView.as_view(url=staticfiles_storage.url('fsw.js'))),
]
