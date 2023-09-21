import mysql.connector

class database():

    def db_start():
        cnx = mysql.connector.connect(
            host='db',
            port=3306,
            user='root',
            password='root'
        )

        create_db_query = 'CREATE DATABASE IF NOT EXISTS promocode'
        cursor = cnx.cursor()
        cursor.execute(create_db_query)

        cnx.database = 'promocode'

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS promocodes (
                id INT PRIMARY KEY AUTO_INCREMENT,
                promocode VARCHAR(30) NOT NULL,
                discount INT NOT NULL
            )
        '''
        cursor.execute(create_table_query)

        select_data_query = 'SELECT COUNT(*) FROM promocodes'
        cursor.execute(select_data_query)
        count = cursor.fetchone()[0]

        if count == 0:
            insert_data_query = '''
                INSERT INTO promocodes (promocode, discount)
                VALUES (%s, %s)
            '''

            data = [
                ('QoEz8sbFKp9jdQrNuXW3', 50),
                ('G6YrA4SMtq7DeWjzCx98', 25),
                ('TnbzWH7fEJpaoYM6kLuX', 75),
                ('KQhjC9e8vBmAPf34LzNu', 10),
                ('XzEa97CvU1TqLKbFSrPh', 30),
                ('L6WgYdF7zqjuA4xEY8Tr', 20),
                ('P2C6Xy9VtkEzBDbfW3L5', 15),
                ('Rn3uhPcAL5tVb69EkXjZ', 60),
                ('F9TZMn7Y1RcNquXhjWsL', 40),
                ('CWHxmqxLF1KT7XQaTBfe', 100)
            ]

            cursor.executemany(insert_data_query, data)

        cnx.commit()

        cursor.close()
        cnx.close()