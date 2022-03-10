from django.shortcuts import render


def client_page(request):
    return render(request, 'client/client.html')
