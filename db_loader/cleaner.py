import psycopg2

import config


conn = psycopg2.connect(host=config.DATABASE_HOST, port=config.DATABASE_PORT, user=config.DATABASE_LOGIN,
                        password=config.DATABASE_PASSWORD, dbname=CONFIG.DATABASE_NAME)
cur = conn.cursor()
cur.execute("truncate client_airconddata;")

conn.commit()
conn.close()
