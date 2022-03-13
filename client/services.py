from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signin(request, username, password):
    try:
        User.objects.get(username=usernamestr)
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return user
    except User.DoesNotExist:
        return f'not_found {username}, {password}'
