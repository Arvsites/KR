from django.urls import path

from . import views

app_name = 'client'
urlpatterns = [
    path('', views.client_page, name='client_page'),
    path('login_page', views.login_page, name='login_page'),
    path('login', views.login_page, name='login')
]
