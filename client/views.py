from django.shortcuts import render
from django.http import HttpResponse
from . import services


def client_page(request, days_to_show=''):
    grafana_data = services.get_data(user, days=days_to_show)
    return render(request, 'client/client.html', {'user': user, 'grafana_data': grafana_data})


def login_page(request):
    return render(request, 'client/login.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = services.signin(request, username, password)
    if isinstance(user, str):
        return HttpResponse(user)

    return client_page(request)
