from django.urls import path

from . import views

app_name = 'client'
urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('client', views.client_page, name='client_page'),
    path('<int:days_to_show>/<str:data_type>', views.client_page, name='client_page'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
