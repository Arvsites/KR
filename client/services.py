from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signin(request, username, password):
    if User.objects.get(username=username):
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return user
    else:
        return 'error'
