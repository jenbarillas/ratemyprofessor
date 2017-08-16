import psycopg2

try:
    conn = psycopg2.connect("dbname='ratemyprofessor' user='bchangip' host='localhost' password='bchangip'")
    conn.autocommit = True;
except:
    print "I am unable to connect to the database"

cur = conn.cursor();



# cur.execute('''INSERT INTO student VALUES (1, 'bchangip', 'Bryan', 'Chan', 'xchangip@gmail.com', 'compu', ARRAY['Progra', 'Musica'], 'Bressani')''')


print("Performing SELECT")
cur.execute('''SELECT firstname FROM student''')

rows = cur.fetchall()

print rows