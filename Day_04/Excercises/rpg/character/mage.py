from abc import ABC, abstractmethod
from .character import Character

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