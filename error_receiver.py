import ast
import time

import paho.mqtt.client as mqtt

import config


# Receiving messages
message_payload = ''


def on_message(client, userdata, message):
    """function for paho.mqtt.client, triggers message"""
    global message_payload
    message_payload = str(message.payload.decode("utf-8"))


def receive(receiver):
    """receives data from errors topic"""
    print("receive")
    receiver.connect(broker_address, port=config.BROKER_PORT)
    receiver.loop_start()

    receiver.subscribe("/errors")
    time.sleep(4)
    receiver.loop_stop()

    if message_payload != '':
        return ast.literal_eval(message_payload)
    else:
        return None


# Setting up an mqtt client
broker_address = config.BROKER_ADDRESS

client = mqtt.Client("error_receiver")
client.username_pw_set(config.BROKER_LOGIN, config.BROKER_PASSWORD)

client.on_message = on_message
