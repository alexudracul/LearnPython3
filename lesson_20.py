# Создайте класс GameCharacter с атрибутами name, health, level и методом speak(),
# который выводит на печать 'Hi, my name is (значение атрибута name)'.
#
# Создайте класс Villain, наследник класса GameCharacter с теми же атрибутами, методом speak(),
# который выводит на печать 'Hi, my name is (значение атрибута name) and I will kill you',
# методом kill(), который принимает в качестве параметра объект класса GameCharacter,
# присваивает атрибуту health этого объекта значение 0 и  выводит на печать 'Bang-bang, now you're dead'


class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is {}'.format(self.name))


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self):
        print('Hi, my name is {} and I will kill you'.format(self.name))

    @staticmethod
    def kill(victim):
        victim.health = 0
        print("Bang-bang, now you're dead")
