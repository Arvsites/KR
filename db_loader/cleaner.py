import psycopg2


conn = psycopg2.connect(host='localhost', port='5432', user='postgres', password='FjhfNB693>M', dbname='kr')
cur = conn.cursor()
cur.execute("truncate client_airconddata;")

conn.commit()
conn.close()
