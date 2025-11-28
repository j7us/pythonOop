# Задание 2

class Sword:
    type = 'Big Sword'
    damage = 35
    element = 'Fire'
    deterioration = 0
    weight = 0

class Equipment:

    def __init__(self, weight, items, max_weight):
        self.weight = weight
        self.items = items
        self.max_weight = max_weight

    def additem(self, item):
        self.items.append(item)

    def updatemaxweight(self, weight):
        self.max_weight = weight

    def throwitem(self):
        item = self.items.pop()
        self.weight = self.weight - item.weight

class Player:

    def __init__(self, name, level, hp, damage, equipment, gold):
        self.name = name
        self.level = level
        self.hp = hp
        self.damage = damage
        self.equipment = equipment
        self.gold = gold

    def heal(self):
        self.hp = 100

    def damageplayer(self, damage_count):
        self.hp -= damage_count

    def addgold(self, gold):
        self.gold += gold

    def additem(self, item):
        self.equipment.additem(item)

def main():
    equipment = Equipment(20, [Sword()], 150)

    first_player = Player("First", 14, 100, 14, equipment, 220)

    first_player.damageplayer(15)
    print(first_player.hp)

    first_player.heal()
    print(first_player.hp)

    first_player.additem(Sword())
    print(equipment.items)

main()