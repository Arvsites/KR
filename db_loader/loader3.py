#!/root/.local/share/virtualenvs/venv-17fYImAv/bin/python3
import json
import paho.mqtt.client as mqtt
import psycopg2
import ast

# receiver
import time

# error_handler
import error_hadler

message_payload = ''


def on_message(client, userdata, message):
    """function for paho.mqtt.client, triggers message"""
    global message_payload
    message_payload = str(message.payload.decode("utf-8"))


broker_address = "37.140.197.191"


def receive(receiver, aircond_num: str):
    """receives data from airconds"""
    receiver.connect(broker_address, port=1883)
    receiver.loop_start()

    receiver.subscribe(f"/device{aircond_num}")
    time.sleep(4)
    receiver.loop_stop()

    if message_payload != '':
        return message_payload
    else:
        return 'error'
#receiver


# mqtt client
client = mqtt.Client("receiver")
client.username_pw_set("KR", "MCiZmQFqf7")

client.on_message = on_message

# postgres client
conn = psycopg2.connect(host='localhost', port='5432', user='postgres', password='FjhfNB693>M', dbname='kr')
cur = conn.cursor()


def load_data(aircond_num: str):
    try:
        data = ast.literal_eval(receive(client, aircond_num))

        errors = error_hadler.analyze_data(data)
        if errors:
            error_hadler.publish_errors(errors)

        cur.execute(f"insert into client_airconddata(time, t1, t2, t3, t4, t5, pressure, cond_id, current, client_id, telegram_chat_id, airconds_count) VALUES (NOW(), {data['t1']}, {data['t2']}, {data['t3']}, {data['t4']}, {data['t5']}, {data['b1']}, 3, {data['i1']}, 6, {data['telegram']}, 2)")
        conn.commit()
    except ValueError:
        pass


while True:
    load_data('3')
