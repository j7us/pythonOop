# Задание 3

class Equipment:

    def __init__(self, weight, items, max_weight):
        self.__weight = weight
        self.__items = items
        self.__max_weight = max_weight

    def additem(self, item):
        self.__items.append(item)

    def updatemaxweight(self, weight):
        self.__max_weight = weight

    def throwitem(self):
        item = self.__items.pop()
        self.__weight = self.__weight - item.weight

class Player:

    def __init__(self, name, level, hp, damage, equipment, gold):
        self.__name = name
        self.__level = level
        self.__hp = hp
        self.__damage = damage
        self.__equipment = equipment
        self.__gold = gold

    def heal(self):
        self.__hp = 100

    def damageplayer(self, damage_count):
        self.__hp -= damage_count

    def addgold(self, gold):
        self.__gold += gold

    def additem(self, item):
        self.__equipment.additem(item)



class Table:
    def __init__(self, length, width, weight):
        self.length = length
        self.width = width
        self.weight = weight

class DiningTable(Table):
    def __init__(self, length, width, weight, serve_seats):
        super().__init__(length, width, weight)
        self.serve_seats = serve_seats

    def add_seat_for_person(self):
        self.serve_seats += 1

    def push_apart(self):
        self.length += 30

class ElectricTable(Table):
    def __init__(self, length, width, weight, height):
        super().__init__(length, width, weight)
        self.height = height


    def increase_height(self, height):
        self.height += height


    def turn_on_power(self):
        print('Стол включен')
