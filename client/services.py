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

    try:
        airconds_count = AircondData.objects.filter(client_login=user_id).first().airconds_count
    except AttributeError:
        return ['кондиционеров не найдено']

    grafana_data_list = []

    if user_id == 1:
        for client in User.objects.all():
            if client.id == 1:
                continue
            first_data_object = AircondData.objects.filter(client_login=client.id).first()
            airconds_count = first_data_object.airconds_count
            for i in range(1, airconds_count * 2 + 1):
                grafana_data_list.append(f"http://37.140.197.191:3000/d-solo/bDeXhSEnk/user{str(client.id)}?orgId=2&from"
                                         f"=now-7d&to=now&theme=dark&viewPanel={str(i)}")
                return grafana_data_list

    for i in range(1, airconds_count * 2 + 1):
        grafana_data_list.append(f"http://37.140.197.191:3000/d-solo/bDeXhSEnk/user{str(user_id)}?orgId=2&from"
                                 f"=now-7d&to=now&theme=dark&viewPanel={str(i)}")

    return grafana_data_list
