# All Items that are available in game

# different types of Items available
class Weapon:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack

class Potion:
    def __init__(self, name, heal, quantity):
        self.name = name
        self.heal = heal
        self.quantity = quantity

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


# All Weapons that are in the game

    # Starter Weapon
newbSword = Weapon('Newb Sword', 3)

basSword = Weapon('Basic Sword', 5)

samSword = Weapon('Samurai Sword', 8)

dank = Weapon('Dank Sword', 13)

# Potions
smallpot = Potion('Small Potion', 50, 1)
medpopt = Potion('Medium Potion', 100, 1)
largepot = Potion('Large Potion', 250, 1)

 #armor