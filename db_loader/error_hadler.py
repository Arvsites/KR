import paho.mqtt.client as mqtt

import config


# check data
MAX_VALUES = {
    't1': 35,
    't2': 35,
    't3': 35,
    't4': 35,
    't5': 35,
    'pressure': 100,
    'current': 100,
}

MIN_VALUES = {
    't1': -30,
    't2': -30,
    't3': -30,
    't4': -30,
    't5': -30,
    'pressure': 50,
    'current': 50,
}


def analyze_data(data: dict):
    """Analyzes data from sensors and detects if there any errors. If some value is more than MAX_VALUE or less than
    MIN_VALUES """
    errors = []

    for key in data.keys():
        n = 1

        if key == 'time' or key == 'cond_id' or key == 'client_id' or key == 'client_id' or key == 'telegram_chat_id' or key == 'airconds_count':
            continue
        if data[key] > MAX_VALUES[key] or data[key] < MIN_VALUES[key]:
            errors.append(f'Датчик {key} выдал аномальное значение {data[key]}! Проверьте, всё ли в порядке.')
        n += 1

    if not errors:
        return

    return [errors, data['telegram_chat_id']]


# send data
broker_address = config.BROKER_ADDRESS

client = mqtt.Client("error_sender")
client.username_pw_set(config.BROKER_LOGIN, config.BROKER_PASSWORD)

client.connect(broker_address, port=config.BROKER_PORT)


def publish_errors(errors: list):
    """Publish errors to mqtt broker"""
    # errors type - [telegram_chat_id, [errors]]
    for error in errors[1]:
        client.publish("errors", {errors[telegram_chat_id]: error})