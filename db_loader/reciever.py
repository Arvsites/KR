import time


message_payload = ''


def on_message(client, userdata, message):
    """function for paho.mqtt.client, triggers message"""
    global message_payload
    message_payload = str(message.payload.decode("utf-8"))


broker_address = "37.140.197.191"


def receive(receiver, aircond_num: str):
    """receives data from airconds"""
    receiver.connect(broker_address)
    receiver.loop_start()

    receiver.subscribe(f"aircond_{aircond_num}")
    time.sleep(0.5)
    receiver.loop_stop()

    return message_payload
