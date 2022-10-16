from django.shortcuts import render
from django.http import HttpResponse
from . import services


def client_page(request, days_to_show='', data_type='graph'):
    grafana_data = services.get_data(request.user, days=days_to_show, data_type=data_type)
    current_data = services.get_current_data(request.user)
    errors = services.get_errors(request.user)
    users = services.get_users(request.user)
    return render(request, 'client/client.html', {'user': request.user,
                                                  'grafana_data': grafana_data,
                                                  'current_data': current_data,
                                                  'errors': errors,
                                                  'users': users})


def login_page(request):
    return render(request, 'client/login.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = services.signin(request, username, password)
    if isinstance(user, str):
        return HttpResponse(user)

    return client_page(request)


def logout(request):
    services.sign_out(request)
    return render(request, 'client/login.html')

