import psycopg2;

conn = psycopg2.connect("host=127.0.0.1 dbname=py_dev user=py_dev password=py_dev")

cur = conn.cursor()

cur.execute("Select * from test;")

print(cur.fetchone())

cur.close
conn.close
