class Game():

    def __init__(self, name, health = 0):
        self.name = name
        self.__health = health
    
    def increment_health(self):
        self.__health += 50

    def print_health(self):
        print(self.__health)
    
    def message(self):
        print("You have selected none.")

class Player(Game):

    def __init__(self, name):
        super().__init__(name, health = 100)
        self.additional = Attribute(101, 200, 300)

    def increment_health(self):
        super().increment_health()
    
    def print_health(self):
        super().print_health()

    def message(self):
        print("You are the player.")


class Enemy(Game):

    def __init__(self, name):
        super().__init__(name, health = 999)

    def message(self):
        print("You are the enemy")

class Attribute(Game):
    def __init__(self, accuracy, stamina, speed):
        self.accuracy = accuracy
        self.stamina = stamina
        self.speed = speed

game = Game(None)
player = Player("Sean")
enemy = Enemy("Goblin")

for x in (game, player, enemy):
    x.message