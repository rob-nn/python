import psycopg2

conn = psycopg2.connect("host=127.0.0.1 dbname=py_dev user=py_dev password=py_dev")

cursor = conn.cursor()

cursor.execute('Create table test(id serial primary key, num integer, data varchar)');

cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
	(100, "abc'def")) 

conn.commit()


cursor.close()

conn.close()

