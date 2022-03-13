from django.shortcuts import render
from django.http import HttpResponse
from . import services


def client_page(request):
    username = request.POST['username']
    password = request.POST['password']

    user = services.signin(request, username, password)

    if user.startswith('not_found'):
        return HttpResponse(user)
    else:
        return render(request, 'client/client.html', {'user': user})


def login_page(request):
    return render(request, 'client/login.html')
