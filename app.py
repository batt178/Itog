from os.path import curdir

import psycopg2
try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='baturin', user='bat', password='mypassword', host='postgres-container', port='5432')
    print('Подключение установлено')
    cursor  = conn.cursor()
    cursor.execute("CREATE TABLE employees (id SERIAL PRIMARY KEY, \
    Name VARCHAR(10), \
    Age INTEGER, \
    Department VARCHAR(50))")
    conn.commit()
    cursor.execute("INSERT INTO employees (Name, Age, Department) VALUES \
    ('Александр', 34, 'Продажи'), \
    ('Мария', 28,'Маркетинг'), \
    ('Иван', 45,'ИТ'), \
    ('Дарья', 23, 'Финансы'), \
    ('Максим', 50, 'Кадры'), \
    ('Анна', 31,'Продажи'), \
    ('Дмитрий', 37, 'Маркетинг'), \
    ('Ольга', 29, 'ИТ'), \
    ('Михаил', 40, 'Финансы'), \
    ('Елена', 26, 'Кадры')")
    conn.commit()
    cursor.execute("SELECT * from employees")
    conn.commit()
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row}")
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Ошибка подключения')
finally:
    if conn:
        cursor.close()
        conn.close()