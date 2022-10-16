import paho.mqtt.client as mqtt

import config

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


def analyze_data(data: dict):
    """Analyzes data from sensors and detects if there any errors. If some value is more than MAX_VALUE or less than
    MIN_VALUES """
    errors = []

    for key in data.keys() :
        if key == 'time' or key == 'cond_id' or key == 'client_id' or key == 'telegram_chat_id' or key == 'airconds_count':
            continue
        if int(data[key]) > MAX_VALUES[key] or int(data[key]) < MIN_VALUES[key] :
            errors.append(f'Датчик {key} выдал аномальное значение {data[key]}! Проверьте, всё ли в порядке.')

    if not errors:
        return
    return errors


def receive(receiver, aircond_num: str):
    """receives data from airconds"""
    receiver.connect(broker_address, port=config.BROKER_PORT)
    receiver.loop_start()

    receiver.subscribe(f"/dev{aircond_num}")
    time.sleep(4)
    receiver.loop_stop()

    if message_payload != '':
        return message_payload
    else:
        return 'error'
