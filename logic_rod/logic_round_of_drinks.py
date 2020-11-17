import os
import time
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from itertools import chain
from collections import defaultdict

from classes_rod.classes_round_of_drinks import Person, Drink, Order
from db_handling_rod.db_handling_round_of_drinks import load_db, read_db, write_db

def get_input(text):
    return input(text)

def people_menu(people_list, drinks_list):
    while True:
        os.system('cls')
        for person in people_list:
            print(person)
        select = input("\n1: Add \n2: Edit or remove \n3: Exit \n")
        if select == "1":
            add_person(people_list, drinks_list)
        elif select == "2":
            edit_arg("person", people_list, drinks_list)
        elif select == "3":
            write_db('people')
            return people_list
        else:
            print("INVALID COMMAND")
            time.sleep(5)

def add_person(people_list, drinks_list):
    os.system('cls')
    for person in people_list:
        print(person)
    temp_first_name = get_input("\nWhat is thier first name? \n    ")
    temp_last_name = get_input("What is thier last name? \n    ")
    try:
        temp_age = get_input("What is thier age? \n    ")
        temp_age = int(temp_age)
        type(temp_age) == type(1)
    except:
       print("That was not an integer")
    # temp_drink = get_input("What is thier race? \n    ")
    print('What is there preferred drink? \n    ')
    temp_drink = preferences(drinks_list)
    person = Person("", temp_first_name, temp_last_name, temp_age, temp_drink)
    people_list.append(person)
    return people_list

def drinks_menu(drinks_list):
    while True:
        os.system('cls')
        for drink in drinks_list:
            print(drink)
        select = input("\n1: Add \n2: Edit or remove \n3: Exit \n")
        if select == "1":
            add_drink(drinks_list)
        elif select == "2":
            edit_arg("drink" ,drinks_list, None)
        elif select == "3":
            write_db('drinks')
            return drinks_list
        else:
            print("INVALID COMMAND")
            time.sleep(5)

def add_drink(drinks_list):
    os.system('cls')
    for drink in drinks_list:
        print(drink)
    temp_name = get_input("\nWhat is its name? \n    ")
    temp_price = get_input("How much does it cost \n    ")
    temp_is_mixer = get_input("Is it a mixer \n    ")
    drink = Drink("", temp_name, float(temp_price), temp_is_mixer)
    drinks_list.append(drink)
    return drinks_list

def edit_arg(list_type ,lst, drinks_list):
    os.system('cls')
    for item in lst:
        print(item)
    obj_selector = {}
    counter = 1
    print(f"\nWhich {list_type} would you like to edit or remove? \n")
    for obj in lst:
        obj_as_list = str(obj).split(", ")
        print(f"{counter}: {obj_as_list[0]}")
        obj_selector[counter] = obj
        counter +=1
    select = int(get_input(""))
    selected_object = obj_selector[select]
    obj_as_list = str(selected_object).split(", ")
    os.system('cls')
    for item in lst:
        print(item)
    print('\nWhich would you like to edit? \n ')
    counter = 1
    for item in obj_as_list:
        print(f"{counter}: {item}")
        counter += 1
    print(f"{counter}: remove")
    choice = get_input("")
    if choice == str(counter):
        lst.remove(selected_object)
    else:
        if (list_type == "person") & (choice == '4'):
            selected_object.race = preferences(drinks_list)
        else:
            change = get_input('what do you want to be changed to? \n   ')
            if list_type == "person":
                if choice == '1':
                    selected_object.first_name = change
                if choice == '2':
                    selected_object.last_name = change
                if choice == '3':
                    selected_object.age = int(change)
            else:
                if choice == '1':
                    selected_object.name = change
                if choice == '2':
                    selected_object.price = float(change)
                if choice == '3':
                    selected_object.is_mixer = change
    return lst

def order_drinks(p_list, d_list, past_orders, is_test = False):
    order_list = []
    name_drink_list = []
    counter = 1
    round_selector = {}
    os.system('cls')
    print("Who is getting the next round? \n")
    for name in p_list:
        print(f"{counter}: {name.first_name}")
        round_selector[counter] = name.first_name
        counter +=1
    select = int(get_input(""))
    order_person = round_selector[select]
    cost = 0
    for name in p_list:
        os.system('cls')
        print(f"What will {name.first_name} have? \n")
        counter = 1
        if name.race != None:
            print(f"{counter}: Thier usual of {name.race}")
            counter +=1
        for drink in d_list:
            print(f"{counter}: {drink.name}")
            counter +=1
        thier_order = get_input("")
        name_drink_list.append(name.first_name)
        if (thier_order == "1") & (name.race != None):
            name_drink_list.append(name.race)
            for drink in d_list:
                if drink.name == name.race:
                    cost += float(drink.price)
        else:
            thier_order = int(thier_order)
            if name.race != None:
                thier_order -= 2
            else:
                thier_order -= 1
            name_drink_list.append(d_list[thier_order].name)
            cost += d_list[thier_order].price
    order_list = Order("", order_person, name_drink_list, cost)
    past_orders.append(order_list)
    if is_test == False:
        write_db('past_orders')
    return order_list

def preferences(d_list):
    counter = 1
    for drink in d_list:
        print(f"{counter}: {drink.name}")
        counter +=1
    thier_preference = get_input("")
    thier_preference = int(thier_preference)
    thier_preference -= 1
    return d_list[thier_preference].name

def stats_menu(people_list, drinks_list, past_orders):
    while True:
        os.system('cls')
        print(F"There are {len(people_list)} poeple")
        print(f"There are {len(drinks_list)} drinks")
        print(f"There has been {len(past_orders)} rounds ordered \n")

        select = input("1: Rounds ordered per person \n2: Drinks by popularity \n3: Average cost of a round per person \n4: Drink's populaity compared to its price \n5: Exit \n")

        if select == "1":
            most_rounds(past_orders)
        elif select == "2":
            drinks_populaity(past_orders)
        elif select == "3":
            average_cost(past_orders)
        elif select == "4":
            populaity_cost(drinks_list, past_orders)
        elif select == "5":
            break

def last_order_tally(order_list):
    x = order_list.people_drinks
    tally = []
    for i in range(len(x)):
        if i % 2 != 0:
            tally.append(x[i])
    tally = dict(Counter(tally))
    return tally

def past_order_tally(past_orders):
    x = []
    tally = []
    for i in past_orders:
        lst = str(i.people_drinks)
        lst = lst.strip("[]")
        lst = lst.split(", ")
        for i in range(len(lst)):
            lst[i] = lst[i].strip("'")
        x += lst
    for i in range(len(x)):
        if i % 2 != 0:
            tally.append(x[i])
    tally = dict(Counter(tally))
    return tally

def most_rounds(past_orders):
    # who buys the most rounds (pie)
    names = ""
    for i in past_orders:
        names += f"{i.person},"
    names = names.split(",")
    names = list(filter(None, names))
    plt.bar(Counter(names).keys(), Counter(names).values())
    plt.xlabel('Person')
    plt.ylabel('Amount Of Rounds Ordered')
    plt.title('Amount Of Rounds Orders Per person')
    plt.show()

def drinks_populaity(past_orders):
    # how many times each drinks has been ordered (pie)
    tally = past_order_tally(past_orders)
    plt.pie(tally.values(), labels = tally.keys())
    plt.title("Drink's Popularity")
    plt.show()

def average_cost(past_orders):
    # average cost of each person round
    results = {}
    for order in past_orders:
        if order.person in results:
            results[order.person].append(order.cost)
        else:
            results[order.person] = [order.cost]
    for result in results:
        plt.bar(result, np.average(results[result]))
    # plt.bar(botttom = 10)
    plt.ylabel('Price (£)')
    plt.title('Average Cost Of A Round Per Person')
    plt.grid(which='major', axis='y')
    plt.show()

def populaity_cost(drinks_list, past_orders):
    # scatter graph with populaity as a percentage against cost
    tally = past_order_tally(past_orders)
    drink_cost = {}
    for drink in drinks_list:
        drink_cost[drink.name] = drink.price
    final_dict = defaultdict(list)
    for k, v in chain(tally.items(), drink_cost.items()):
        final_dict[k].append(v)
    results = list(final_dict.values())
    results_names = list(final_dict.keys())
    for i in range(len(results)):
        if len(results[i]) == 2:
            plt.scatter(results[i][0], results[i][1], label = results_names[i])
    plt.xlabel('Amount Of Orders')
    plt.ylabel('Price (£)')
    plt.title('Amount Of Orders Against Price')
    plt.legend(results_names)
    plt.grid()
    plt.show()