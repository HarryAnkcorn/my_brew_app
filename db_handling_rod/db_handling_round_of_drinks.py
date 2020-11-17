import pymysql

from classes_rod.classes_round_of_drinks import Person, Drink, Order

people_list = []
drinks_list = []
past_orders = []

def load_db():
    data = read_db("people")
    for line in data:
        people_list.append(Person(line[0], line[1], line[2], line[3], line[4]))
    data = read_db("drinks")
    for line in data:
        drinks_list.append(Drink(line[0], line[1], line[2], line[3]))
    data = read_db("past_orders")
    for line in data:
        past_orders.append(Order(line[0], line[1], line[2], line[3]))
    return people_list, drinks_list, past_orders

def connect_to_db():
    connection = pymysql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "password",
    db = "brew",
    charset='utf8mb4',
    )
    return connection

def read_db(table_name):
    connection = connect_to_db()

    data = []
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def write_db(table_name):
    connection = connect_to_db()

    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    if "people" in table_name:
        for person in people_list:
            cursor.execute(f"INSERT INTO people () values (NULL, '{person.first_name}', '{person.last_name}', '{person.age}', '{person.race}')")
    elif "drink" in table_name:
        for drink in drinks_list:
            cursor.execute(f"INSERT INTO drinks () values (NULL, '{drink.name}', '{drink.price}', '{drink.is_mixer}')")
    else:
        for order in past_orders:
            cursor.execute(f"""INSERT INTO past_orders () values (NULL, '{order.person}', "{order.people_drinks}", '{order.cost}')""")

    connection.commit()
    cursor.close()
    connection.close()