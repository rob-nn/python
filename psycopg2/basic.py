import psycopg2

conn = psycopg2. connect(database='my_django', user='appserver', password='appserver', host='192.168.1.2')

cur = conn.cursor()

cur.execute("select * from table_a;")

for reg in cur.fetchall():
    print (reg)
 
cur.close()
conn.close()
