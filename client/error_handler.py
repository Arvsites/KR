import time
import ast

import paho.mqtt.client as mqtt

from . import config_mqtt

# check data
MAX_VALUES = {
    't1': 25,
    't2': 25,
    't3': 25,
    't4': 25,
    't5': 25,
    'b1': 90,
    'i1': 25,
}

MIN_VALUES = {
    't1': -10,
    't2': -10,
    't3': -10,
    't4': -10,
    't5': -10,
    'b1': 55,
    'i1': -10,
}


def analyze_data(data: dict, username: str, cond_id: str):
    """Analyzes data from sensors and detects if there any errors. If some value is more than MAX_VALUE or less than
    MIN_VALUES """
    errors = {}

    if not data:
        return {f"Ошибки  {username}, кондиционер с id {cond_id}: ": "Ошибки отсутствуют"}

    for key in ast.literal_eval(data.keys()):
        if key == 'time' or key == 'cond_id' or key == 'client_id' or key == 'telegram_chat_id' or key == 'airconds_count':
            continue
        if int(data[key]) > MAX_VALUES[key] or int(data[key]) < MIN_VALUES[key] :
            errors[f"Ошибки  {username}, кондиционер с id {cond_id}, датчик {key}: "] = f'Датчик {key} выдал аномальное значение {data[key]}! Проверьте, всё ли в порядке.'

    if not errors:
        return
    return errors


message_payload = ''


def receive(receiver, aircond_num: str):
    """receives data from airconds"""
    receiver.connect(config_mqtt.BROKER_ADDRESS, port=config_mqtt.BROKER_PORT)
    receiver.loop_start()

    receiver.subscribe(f"/dev{aircond_num}")
    time.sleep(2)
    receiver.loop_stop()

    if message_payload != '':
        return message_payload
    else:
        return False
