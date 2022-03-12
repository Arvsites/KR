from django.shortcuts import render

from . import services


def client_page(request):
    return render(request, 'client/client.html')


def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = services.signin(request, username, password)

    return render(request, 'client/login.html', {'user': user})
