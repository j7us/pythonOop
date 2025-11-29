import random
# Рефлексия занятия 3

# По невнимательности я пропустил условие о создании двух примеров наследования, ниже будет исправленная версия

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


class Chair:
    def __init__(self, material):
        self.seat = material

class ComputerChair(Chair):
    def __init__(self, material, height, tilt_angle):
        super().__init__(material)
        self.height = height
        self.tilt_angle = tilt_angle

    def change_angle(self, angle):
        self.tilt_angle = angle

    def change_height(self, height):
        self.height = height


class RockingChair(Chair):
    def __init__(self, material):
        super().__init__(material)


# Задание 4

# 4.1

# Создадим класс комната, в которой нам нужно установить стол и стул

class Room:
    def __init__(self, table, chair):
        self.table = table
        self.chair = chair

# В данном случае мы используем композицию, передавая в объект Room объекты table и chair,
# а также оставляем задел на полиморфизм, если нам понадобится вызывать общий метод для классов
# стола или стула, то мы сможем переопределить его в наследниках этих классов и вызывать эти методы
# в зависимости от переданного типа стола/стула
def init_room() -> Room:
    table = ElectricTable(54, 16,22, 40)
    chair = ComputerChair('Пластик', 37, 45)

    return Room(table, chair)


# 4.2

# В данном примере в качестве полиморфизма подтипов представлен вызов метода animal.foo(), который переопределен
# в классах Cat и Bird и его выполнение будет зависеть именно от типа, который мы передали (любого наследника класса Animal).
# А в качестве параметрического полиморфизма представлен сам метод do_something_with_animal, который принимает любой
# класс, наследуемый от Animal и как-то с ним работает внутри себя

# 4.3

class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def random_animal(animals: list[Animal]):
    animals.clear()

    for x in range(500):
        animals.append(Cat() if random.randint(1, 17) % 2 == 0  else Bird())

animals_start = [Cat(), Bird()]
random_animal(animals_start)

for animal in animals_start:
    animal.foo()

# В результате мы получаем либо "Кошка мурлычет", либо "Птица поет" благодаря полиморфизму и переопределенному методу foo