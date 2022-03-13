from django.shortcuts import render
from django.http import HttpResponse
from . import services


def client_page(request):
    usernamestr = request.POST.get('username')
    password = request.POST.get('password')

    user = services.signin(request, usernamestr, password)

    if user == 'not_found':
        return HttpResponse('Пользователь не найден')
    else:
        return render(request, 'client/client.html', {'user': user})


def login_page(request):
    return render(request, 'client/login.html')
