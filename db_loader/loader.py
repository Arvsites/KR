import json
import paho.mqtt.client as mqtt
import psycopg2

import db_loader.reciever as receiver


# mqtt client
client = mqtt.Client("receiver")
client.on_message = receiver.on_message

# postgres client
conn = psycopg2.connect("dbname=kr user=postgres")
cur = conn.cursor()


def load_data(aircond_num: str):
    data = json.loads(receiver.receive(client, aircond_num))
    cur.execute(f"insert into aircond_{aircond_num}(time, t1, t2, t3, t4, t5, pressure, c1, c2, current)"
                f"VALUES ({data['time1']}, {data['t1']}, {data['t2']}, {data['t3']}, {data['t4']}, {data['t5']},"
                f"{data['b1']}, {data['i1']}, {data['i1']}, {data['current']})")
    cur.close()
