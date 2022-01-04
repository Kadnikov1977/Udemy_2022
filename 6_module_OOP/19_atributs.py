class Char:
    def __init__(self, username, race, klass, gold):
        self.username = username
        self.race = race
        self.klass = klass
        self.gold = gold



char001 = Char('HarryChpoker', 'Orc', 'Druid', 1)
char002 = Char('HarryPoter', 'Human', 'Paladin', 2)

char001.gold = 3
char002.gold = 4

print(char001.gold)
print(char002.gold)
