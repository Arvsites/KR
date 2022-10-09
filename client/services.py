from django.contrib.auth.models import User

from .models import Airconddata
from django.contrib.auth import authenticate, login, logout


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


def sign_out(request):
    logout(request)


def get_days_link(days):
    if days == 1:
        return 'now-1d'
    if days == 1:
        return 'now-7d'


def get_data(user, days='', data_type='graph'):
    """Get data for showing grafana graphics"""

    grafana_links_parts = {'user2': 'pr5Ye79nz', 'user3': '3B_3gV9nk'} # parts of user's panel's id

    user_id = user.id
    # list of links to get grafana's data
    grafana_data_list = []

    if days:
        days_to_show = get_days_link(days)
    else:
        days_to_show = 'now-1d'

    # counter to define from which grafana's panelId we should start
    counter: list
    if data_type == 'graph':
        counter = [1, 3]
    if data_type == 'table':
        counter = [4, 6]

    if user_id == 1:
        for client in User.objects.all():
            if client.id == 1:
                continue

            airconds_count = Airconddata.objects.filter(client=client.id).first().airconds_count
            if airconds_count == 1:
                for i in range(counter[0], counter[1]):
                    if client.id == 2:
                        grafana_data_list.append(
                            f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user2']}/user{client.id}?orgId"
                            f"=2&from"
                            f"={days_to_show}&to=now&theme=dark&panelId={i}")

            else:
                for i in range(1, airconds_count * 2 + 1):
                    if client.id == 3:
                        grafana_data_list.append(
                            f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user3']}/user{client.id}?orgId"
                            f"=2&from"
                            f"={days_to_show}&to=now&theme=dark&panelId={i}")

        return grafana_data_list

    airconds_count = Airconddata.objects.filter(client=user_id).first().airconds_count

    if airconds_count == 1:
        for i in range(counter[0], counter[1]):
            if user_id == 2:
                grafana_data_list.append(
                    f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user2']}/user{user_id}?orgId"
                    f"=2&from"
                    f"={days_to_show}&to=now&theme=dark&panelId={i}")

    else:
        for i in range(1, airconds_count * 3 + 1):
            if user_id == 3:
                grafana_data_list.append(
                    f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user3']}/user{user_id}?orgId"
                    f"=2&from"
                    f"={days_to_show}&to=now&theme=dark&panelId={i}")

    return grafana_data_list
