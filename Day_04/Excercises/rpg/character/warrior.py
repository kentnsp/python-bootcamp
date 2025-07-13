from abc import ABC, abstractmethod
from .character import Character

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