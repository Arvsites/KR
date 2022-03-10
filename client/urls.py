from django.urls import path

from . import views

app_name = 'client'
urlpatterns = [
    path('', views.client_page, name='client_page')
]
