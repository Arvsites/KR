from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signin(request, username, password):
    try:
        User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return user
        else:
            return 'wrong password'
    except User.DoesNotExist:
        return 'user not found'
