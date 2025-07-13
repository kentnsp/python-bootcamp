from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health = 100, defense = 10):
        self.health = health
        self.defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

class Knight(Character):
    def attack(self, other):
        print("Opponent initial health: ", other.health)
        damage = self.defense - other.defense
        print("Knight Damage Dealt: ", damage)
        other.health -= damage
        print("Opponent final health: ", other.health)
        print()

class Mage(Character):
    def __init__(self, magic = 5):
        super().__init__()
        self.magic = magic

    def attack(self, other):
        print("Opponent initial health: ", other.health)
        damage = (self.defense + self.magic) - other.defense
        print("Mage Damage Dealt: ", damage)

        other.health -= damage
        print("Opponent final health: ", other. health)
        print()

class Warrior(Character):
    def __init__(self,  strength=10):
        super().__init__()
        self.strength = strength

    def attack(self, other):
        print("Opponent initial health: ", other.health)
        damage = (self.defense * self.strength) - other.defense
        print("Warrior Damage Dealt: ", damage)
        other.health -= damage
        print("Opponent final health: ", other.health)
        print()


knight2 = Knight()
mage1 = Mage()
warrior1 = Warrior()

print("Knight vs Mage")
knight2.attack(mage1)

print("Mage vs Warrior")
mage1.attack(warrior1)

print("Warrior vs Knight")
warrior1.attack(knight2)