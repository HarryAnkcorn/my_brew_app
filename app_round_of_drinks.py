import os
import time
from collections import Counter

from db_handling_rod.db_handling_round_of_drinks import load_db
from logic_rod.logic_round_of_drinks import last_order_tally, people_menu, drinks_menu, order_drinks, stats_menu
# from classes_rod.classes_round_of_drinks import Order

people_list = []
drinks_list = []
order_list = []
past_orders = []

load_check = False
new_order = False

while True:
    os.system('cls')
    if load_check == False:
        people_list, drinks_list, past_orders = load_db()
        load_check = True
        continue
    
    if order_list != []:
        if new_order == True:
            tally = last_order_tally(order_list)
        print(f'Latest round: {order_list.person}, {tally}, £{"%.2f" % order_list.cost} \n')

    select = input("""1: People menu
2: Drinks menu 
3: Order a round 
4: Stats 
5: Exit 
""")

    if select == "1":
        people_menu(people_list, drinks_list)
    elif select == "2":
        drinks_menu(drinks_list)
    elif select == "3":
        order_list = order_drinks(people_list, drinks_list, past_orders)
        new_order = True
    elif select == "4":
        stats_menu(people_list, drinks_list, past_orders)
    elif select == "5":
        os.system('cls')
        exit()
    else:
        print("INVALID COMMAND")
        time.sleep(5)

# ideas:
# for ordering it should show thier perfences with the oppostion to make the round the same as thier everybody preferences
# fix "your usual of None"
# error when not selecting a drink, out of range index
# click ENTER to select the preference drink or skip
# export a fancy list
# code deletes all the rows then writes all new rows
# ids keep increasing
# if a drink is a spirit then it goes with a mixer
# put in try and expects