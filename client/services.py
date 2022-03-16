from django.contrib.auth.models import User

from .models import AircondData
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


def get_data(user):
    """Get data for showing grafana graphics"""
    user_id = user.id
    temperature = f"http://37.140.197.191:3000/d-solo/bDeXhSEnk/aircond{str(user_id)}?orgId=2&from=now-7d&to" \
                 f"=now&theme=dark&panelId=2"
    return {'temperature': temperature}
