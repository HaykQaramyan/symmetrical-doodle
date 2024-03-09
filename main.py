import psycopg2
connect=psycopg2.connect(
    host='localhost',
    user='postgres',
    password='password',
    database='think_test_db'
)
cursor = connect.cursor()
print('OK!')


def data_into_users(name, email, birthday, password):
    cursor.execute("INSERT INTO users (name, email, birthday, password) VALUES (%s, %s, %s, %s)",
                   (name, email, birthday, password))
    connect.commit()

# data_into_users('Iosif', 'Iosif.1991@gmail.com', '1991-11-30', 'IosifBerlin')


def update_user(id, n_name, n_email, n_birthday, n_password):
    cursor.execute("UPDATE users SET name = %s, email = %s, birthday = %s, password = %s WHERE id = %s ",
                   (n_name, n_email, n_birthday, n_password, id))
    connect.commit()

update_user(2, 'Armen', 'Armen@gmail.com', '1999-11-22','12345678')