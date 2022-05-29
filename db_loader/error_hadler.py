import paho.mqtt.client as mqtt

import config

# check data
MAX_VALUES = {
    't1' : 35,
    't2' : 35,
    't3' : 35,
    't4' : 35,
    't5' : 35,
    'b1' : 100,
    'i1' : 100,
}

MIN_VALUES = {
    't1' : -30,
    't2' : -30,
    't3' : -30,
    't4' : -30,
    't5' : -30,
    'b1' : 50,
    'i1' : 50,
}


def analyze_data(data: dict) :
    """Analyzes data from sensors and detects if there any errors. If some value is more than MAX_VALUE or less than
    MIN_VALUES """
    print("analyze data")
    errors = []

    for key in data.keys() :
        if key == 'time' or key == 'cond_id' or key == 'client_id' or key == 'telegram_chat_id' or key == 'airconds_count':
            continue
        if int(data[key]) > MAX_VALUES[key] or int(data[key]) < MIN_VALUES[key] :
            errors.append(f'Датчик {key} выдал аномальное значение {data[key]}! Проверьте, всё ли в порядке.')

    if not errors :
        return

    return [data['telegram_chat_id'], errors]


# send data
broker_address = config.BROKER_ADDRESS

client = mqtt.Client("error_sender")
client.username_pw_set(config.BROKER_LOGIN, config.BROKER_PASSWORD)

client.connect(broker_address, port=config.BROKER_PORT)


def publish_errors(errors: list) :
    """Publish errors to mqtt broker"""
    # errors type - [telegram_chat_id, [errors]]
    for error in errors[1] :
        print("sending error")
        client.publish("/errors", {str(errors[0]) : error})
