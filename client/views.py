from django.shortcuts import render


def client_page(request):
    return render(request, 'client/client.html')


def login_page(request):
    return render(request, 'client/login.html')
