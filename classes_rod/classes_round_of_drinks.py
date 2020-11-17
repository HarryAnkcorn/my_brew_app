class Person:
    def __init__(self, person_id, first_name, last_name, age, race):
        self.person_id = person_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.race = race
    
    def __repr__(self):
        return (f"{self.first_name}, {self.last_name}, {self.age}, {self.race}")

class Drink:
    def __init__(self, drink_id, name, price, is_mixer):
        self.drink_id = drink_id
        self.name = name
        self.price = price
        self.is_mixer = is_mixer
    
    def __repr__(self):
        return (f"{self.name}, £{'%.2f' % self.price}, {self.is_mixer}")

class Order:
    def __init__(self, order_id, person, people_drinks, cost):
        self.order_id = order_id
        self.person = person
        self.people_drinks = people_drinks
        self.cost = cost
        
    def __repr__(self):
        return (f"{self.person}, {self.people_drinks}, £{'%.2f' % self.cost}")