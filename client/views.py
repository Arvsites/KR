from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import services


def client_page(request, days_to_show='', data_type='graph'):
    user = request.user
    if services.check_anonymous(user):
        grafana_data = services.get_data(user, days=days_to_show, data_type=data_type)
        current_data = services.get_current_data(user)
        errors = services.get_errors(user)
        users = services.get_users(user)
        return render(request, 'client/client.html', {'user': request.user,
                                                      'grafana_data': grafana_data,
                                                      'current_data': current_data,
                                                      'errors': errors,
                                                      'users': users})
    else:
        return redirect('/')


def login_page(request):
    return render(request, '/')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = services.signin(request, username, password)
    if isinstance(user, str):
        return HttpResponse(user)

    return redirect('/client')


def logout(request):
    services.sign_out(request)
    return redirect('/')

