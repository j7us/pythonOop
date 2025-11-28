# Задание 1.1
# Telegram может содержать классы User с хранением id пользователя и связанной с ним информацией,
# класс Chat, в котором будут поля с уникальныйм id чата, список последних подгруженных сообщений и id
# пользователей, которые состоят в чате


# Задание 1.2
class Sword:
    type = 'Big Sword'
    damage = 35
    element = 'Fire'
    deterioration = 0

class Equipment:
    weight = 15
    max_weight = 200
    items = [Sword()]

class Player:
    name = 'OrkKiller'
    level = 25
    hp = 100
    damage = 50
    equipment = Equipment()
    gold = 200


# Задание 1.3

def main():

    # Создаем новый меч
    new_sword = Sword()

    # Передаем его в использование
    usage_sword = new_sword

    # Меч изнашивается
    usage_sword.deterioration = 55

    # Если меч износился больше, чем на 40% его урон уменьшается
    if usage_sword.deterioration > 40:
        usage_sword.damage = 20

    # Урон нового меча уменьшился
    print(new_sword.damage)

main()

