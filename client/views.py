from django.shortcuts import render
from django.http import HttpResponse
from . import services


def client_page(request):
    return render(request, 'client/client.html')


def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = services.signin(request, username, password)

    if user == 'not_found':
        return HttpResponse('Пользователь не найден')
    else:
        return render(request, 'client/login.html', {'user': user})
