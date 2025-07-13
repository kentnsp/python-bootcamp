from character.knight import Knight
from character.mage import Mage
from character.warrior import Warrior

knight1 = Knight()
mage1 = Mage()
warrior1 = Warrior()

print("Knight vs Mage")
knight1.attack(mage1)

print("Mage vs Warrior")
mage1.attack(warrior1)

print("Warrior vs Knight")
warrior1.attack(knight1)