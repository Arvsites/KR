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
    grafana_links_parts = {'user5': 'P3c0ghPnz', 'user6': 'UC6uihP7z'}
    """Get data for showing grafana graphics"""
    user_id = user.id
    grafana_data_list = []

    if user_id == 1:
        for client in User.objects.all():
            if client.id == 1 or client.id == 5:
                continue

            airconds_count = Airconddata.objects.filter(client=client.id).first().airconds_count
            for i in range(1, airconds_count + 1):
                for z in range(1, 4):
                    if client.id == 6:
                        grafana_data_list.append(
                            f"http://37.140.197.191:3000/d-solo/{grafana_links_parts['user6']}/user{client.id}?orgId"
                            f"=2&from "
                            f"=now-7d&to=now&theme=dark&panelId={z}")
                    if client.id == 5:
                        grafana_data_list.append(
                            f"http://37.140.197.191:3000/d-solo/{grafana_links_parts['user5']}/user{client.id}?orgId"
                            f"=2&from "
                            f"=now-7d&to=now&theme=dark&panelId={z}")

            return grafana_data_list

    airconds_count = Airconddata.objects.filter(client=user_id).first().airconds_count
    for i in range(1, airconds_count + 1):
        for z in range(1, 4):
            if user_id == 6:
                grafana_data_list.append(
                    f"http://37.140.197.191:3000/d-solo/{grafana_links_parts['user6']}/user{user_id}?orgId"
                    f"=2&from "
                    f"=now-7d&to=now&theme=dark&panelId={z}")
            if user_id == 5:
                grafana_data_list.append(
                    f"http://37.140.197.191:3000/d-solo/{grafana_links_parts['user5']}/user{user_id}?orgId"
                    f"=2&from "
                    f"=now-7d&to=now&theme=dark&panelId={z}")

    return grafana_data_list
