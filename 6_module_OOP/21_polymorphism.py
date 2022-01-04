# class Char_for_all:
#     def __init__(self, username, health, agility):
#         self.username = username
#         self.health = health
#         self.agility = agility
#         self.gold = 0
#
#
# class Char_with_race(Char_for_all):
#     def __init__(self, username, health, agility, race):
#         Char_for_all.__init__(self, username, health, agility)
#         self.race = race
#         if self.race == 'orc':
#             self.health += 50
#         if self.race == 'night elf':
#             self.agility += 50
#
#
# char1 = Char_with_race('HarryChpoker', 30, 30, 'orc')
# char2 = Char_with_race('HarryPoter', 30, 30, 'night elf')
# print(char1.health, char1.agility)
# print(char2.health, char2.agility)


class GameCharacter:

    def __init__(self, name, health,
                 level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is ' + self.name)


class Villain(GameCharacter):

    def __init__(self, name, health,
                 level):
        GameCharacter.__init__(self, name, health,
                               level)

    def speak(self):
        print('Hi, my name is ' + self.name + ' and I will kill you')

    def kill(self, other):
        other.health = 0
        print('Bang-bang, now you\'re dead')


james = GameCharacter('James', 100, 1)
jim = Villain('Jim', 100, 2)

james.speak()
jim.speak()
print(james.health)
jim.kill(james)
print(james.health)