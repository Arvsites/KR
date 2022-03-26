from django.contrib.auth.models import User

from .models import Airconddata
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
    grafana_links_parts = {'user2': 'O3upqisnk', 'user3': '_Is_3msnk'}
    """Get data for showing grafana graphics"""
    user_id = user.id
    grafana_data_list = []

    if user_id == 1:
        for client in User.objects.all():
            if client.id == 1:
                print(1)
                continue

            airconds_count = Airconddata.objects.filter(client=client.id).first().airconds_count
            if airconds_count == 1:
                for i in range(1, 4):
                    if user_id == 2:
                        grafana_data_list.append(
                            f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user2']}/user{user_id}?orgId"
                            f"=1&from"
                            f"=now-7d&to=now&theme=dark&panelId={i}")

            else:
                for i in range(1, airconds_count * 3 + 1):
                    if user_id == 3:
                        grafana_data_list.append(
                            f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user3']}/user{user_id}?orgId"
                            f"=1&from"
                            f"=now-7d&to=now&theme=dark&panelId={i}")

        return grafana_data_list

    airconds_count = Airconddata.objects.filter(client=user_id).first().airconds_count

    if airconds_count == 1:
        for i in range(1, 4):
            if user_id == 2:
                grafana_data_list.append(
                    f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user2']}/user{user_id}?orgId"
                    f"=1&from"
                    f"=now-7d&to=now&theme=dark&panelId={i}")

    else:
        for i in range(1, airconds_count * 3 + 1):
            if user_id == 3:
                grafana_data_list.append(
                    f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user3']}/user{user_id}?orgId"
                    f"=1&from"
                    f"=now-7d&to=now&theme=dark&panelId={i}")

    return grafana_data_list
