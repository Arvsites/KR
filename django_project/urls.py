from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
    path('', include('pwa.urls')),
    path('favicon.ico', RedirectView.as_view(url=static('favicon.ico'))),
]
