from django.contrib.auth.models import User

from .models import Airconddata
from django.contrib.auth import authenticate, login, logout

import paho.mqtt.client as mqtt
from . import config_mqtt
from . import error_handler


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
    if days == 7:
        return 'now-7d'


def get_panelId_counter(data_type, airconds_count):
    if data_type == 'graph':
        # formula to detect from which to which graph or table get data from grafana
        return {"user2": [1, airconds_count * 2 + 1], "user3": [1, airconds_count * 2 + 1]}
    if data_type == 'table':
        return {"user2": [airconds_count * 2 + 1, 2 * (airconds_count * 2 + 1) - 1],
                "user3": [airconds_count * 2 + 1, 2 * (airconds_count * 2 + 1) - 1]}


def get_data(user, days='', data_type='graph'):
    """Get data for showing grafana graphics"""

    # parts of user's panel's id
    grafana_links_parts = {'user2': 'pr5Ye79nz', 'user3': '3B_3gV9nk'}

    # counter to define from which grafana's panelId we should start
    user_id = user.id

    # list of links to get grafana's data
    grafana_data_list = []

    if days:
        days_to_show = get_days_link(days)
    else:
        days_to_show = 'now-1d'

    if user_id == 1:
        for client in User.objects.all():
            if client.id == 1:
                continue

            airconds_count = Airconddata.objects.filter(client=client.id).first().airconds_count
            counter = get_panelId_counter(data_type,  airconds_count)

            if airconds_count == 1:
                for i in range(counter["user2"][0], counter["user2"][1]):
                    if client.id == 2:
                        grafana_data_list.append(
                            f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user2']}/user{client.id}?orgId"
                            f"=2&from"
                            f"={days_to_show}&to=now&theme=dark&panelId={i}")

            else:
                for i in range(counter["user3"][0], counter["user3"][1]):
                    if client.id == 3:
                        grafana_data_list.append(
                            f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user3']}/user{client.id}?orgId"
                            f"=2&from"
                            f"={days_to_show}&to=now&theme=dark&panelId={i}")

        return grafana_data_list

    airconds_count = Airconddata.objects.filter(client=user_id).first().airconds_count
    counter = get_panelId_counter(data_type, airconds_count)

    if airconds_count == 1:
        for i in range(counter["user2"][0], counter["user2"][1]):
            if user_id == 2:
                grafana_data_list.append(
                    f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user2']}/user{user_id}?orgId"
                    f"=2&from"
                    f"={days_to_show}&to=now&theme=dark&panelId={i}")

    else:
        for i in range(counter["user3"][0], counter["user3"][1]):
            if user_id == 3:
                grafana_data_list.append(
                    f"https://multimer.ru:3000/d-solo/{grafana_links_parts['user3']}/user{user_id}?orgId"
                    f"=2&from"
                    f"={days_to_show}&to=now&theme=dark&panelId={i}")

    return grafana_data_list


def get_current_data(user):
    """Gets current aircond's data from postgresql"""

    # check if user is admin and the don't return any data
    if user.id == 1:
        return {}
    else:
        data = Airconddata.objects.filter(client=user.id).latest('id')
        return {
                "t1": data.t1,
                "t2": data.t2,
                "t3": data.t3,
                "t4": data.t4,
                "t5": data.t5,
                "i1": data.current,
                "b1": data.pressure
                }


def get_errors(user):
    broker_address = config_mqtt.BROKER_ADDRESS

    client = mqtt.Client("error_sender_site")
    client.username_pw_set(config_mqtt.BROKER_LOGIN, config_mqtt.BROKER_PASSWORD)

    client.connect(broker_address, port=config_mqtt.BROKER_PORT)

    # check if user is admin and the don't return any data
    if user.id == 1:
        errors = {}
        for client in User.objects.all():
            if client.id == 1:
                continue

            if client.id == 2:
                cond_id = Airconddata.objects.filter(client=user.id).latest('cond_id')
                data = error_handler.receive(client, str(cond_id))
                errors[f"{client.id}"] = error_hadler.analyze_data(data)

            if client.id == 3:
                data = error_handler.receive(client, "2")
                errors = error_hadler.analyze_data(data)
                data = error_handler.receive(client, "3")
                errors[f"{client.id}"] = error_hadler.analyze_data(data)

        return errors

    if user.id == 2:
        data = error_handler.receive(client, "1")
        errors = error_hadler.analyze_data(data)

        return {f"{user.id}": errors}
    if user.id == 3:
        data = error_handler.receive(client, "2")
        errors = error_hadler.analyze_data(data)
        data = error_handler.receive(client, "3")
        errors.append(error_hadler.analyze_data(data))

        return errors
