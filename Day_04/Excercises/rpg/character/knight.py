from abc import ABC, abstractmethod
from .character import Character

class Knight(Character):

    def attack(self, other):
        print("Opponent initial health: ", other.health)
        damage = self.defense - other.defense
        print("Knight Damage Dealt: ", damage)
        other.health -= damage
        print("Opponent final health: ", other.health)
        print()
