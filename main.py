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

# data_into_users('Vazgen', 'Vazgen.99@gmail.com', '1987-05-22', 'Vazgenchoo123')
data_into_users('Iosif', 'Iosif.1991@gmail.com', '1991-11-30', 'IosifBerlin')
# data_into_users('Bavakan', 'Bavakan.2001@gmail.com', '2001-09-11', 'Bavakan228')
