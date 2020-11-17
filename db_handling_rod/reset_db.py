import pymysql
import os

os.system('cls')

def reset():
    connection = pymysql.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "password",
        db = "brew",
        charset='utf8mb4'
        )

    cursor = connection.cursor()

    cursor.execute("DROP TABLE people")
    cursor.execute("""CREATE TABLE people (
        person_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        age INTEGER,
        race VARCHAR(100))
    """)

    cursor.execute("INSERT INTO people () values (NULL, 'Frodo', 'Baggins', 50, 'Gin')")
    cursor.execute("INSERT INTO people () values (NULL, 'Samwise', 'Gamgee', 38,'Beer')")
    cursor.execute("INSERT INTO people () values (NULL, 'Merry', 'Brandybuck', 36, 'Cider')")
    cursor.execute("INSERT INTO people () values (NULL, 'Pippin', 'Took', 28,'Beer')")

    cursor.execute("DROP TABLE drinks")
    cursor.execute("""CREATE TABLE drinks (
        drink_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        price FLOAT,
        is_mixer VARCHAR(100))
    """)

    cursor.execute("INSERT INTO drinks () values (NULL, 'Beer', 3.2, 'no')")
    cursor.execute("INSERT INTO drinks () values (NULL, 'Cider', 3.5, 'no')")
    cursor.execute("INSERT INTO drinks () values (NULL, 'Gin', 5.0, 'no')")
    cursor.execute("INSERT INTO drinks () values (NULL, 'Vodka', 4.2, 'no')")
    cursor.execute("INSERT INTO drinks () values (NULL, 'Coke', 2.7, 'yes')")
    cursor.execute("INSERT INTO drinks () values (NULL, 'Lemonade', 2.6, 'yes')")

    cursor.execute("DROP TABLE past_orders")
    cursor.execute("""CREATE TABLE past_orders (
        order_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        person VARCHAR(100),
        people_drinks VARCHAR(100),
        price FLOAT)
    """)

    cursor.execute("""INSERT INTO past_orders () values (
        NULL, 'Frodo', "['Frodo', 'Beer', 'Samwise', 'Beer', 'Merry', 'Beer', 'Pippin', 'Beer']", 12.80)""")
    cursor.execute("""INSERT INTO past_orders () values (
        NULL, 'Samwise', "['Frodo', 'Beer', 'Samwise', 'Beer', 'Merry', 'Beer', 'Pippin', 'Beer']", 12.80)""")
    cursor.execute("""INSERT INTO past_orders () values (
        NULL, 'Merry', "['Frodo', 'Beer', 'Samwise', 'Beer', 'Merry', 'Cider', 'Pippin', 'Cider']", 13.40)""")
    cursor.execute("""INSERT INTO past_orders () values (
        NULL, 'Pippen', "['Frodo', 'Gin', 'Samwise', 'Gin', 'Merry', 'Vodka', 'Pippin', 'Vodka']", 18.40)""")
    cursor.execute("""INSERT INTO past_orders () values (
        NULL, 'Frodo', "['Frodo', 'Coke', 'Samwise', 'Lemonade', 'Merry', 'Lemonade', 'Pippin', 'Lemonade']", 10.5)""")

    connection.commit()
    cursor.close()
    connection.close()

reset()