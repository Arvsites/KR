from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signin(request, usernamestr, password):
    try:
        User.objects.get(username=usernamestr)
        user = authenticate(request, username=usernamestr, password=password)
        login(request, user)
        return user
    except User.DoesNotExist:
        return 'not_found'
