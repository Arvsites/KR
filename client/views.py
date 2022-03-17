from django.shortcuts import render
from django.http import HttpResponse
from . import services


def client_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = services.signin(request, username, password)

    if isinstance(user, str):
        return HttpResponse(user)
    else:
        grafana_data = services.get_data(user)
        if len(grafana_data) == 1:
            return HttpResponse(f'У пользователя {username} с id {user.id} нет кондиционеров')
        return render(request, 'client/client.html', {'user': user, 'grafana_data': grafana_data})


def login_page(request):
    return render(request, 'client/login.html')
