from __future__ import print_function
import sys, time as t
from random import randint
from extras.menu import battleMenu, mainMenu
from extras.items import *
from extras.characters import *


# Player Starting Stats


welcomeString = """\nWelcome to the game %s! \nThe objective of the game is to slay the dragon.
    """ % hero.name
print(welcomeString)
t.sleep(1.5)
# Confirms that the user actually wants to continue
confirmation = raw_input("\nDo you believe that you are up to the task?(yes or no) ")
t.sleep(1)
if confirmation == 'yes':
    print("\nSounds great! Let's get started!")
elif confirmation == 'no':
    print("Alright, be sure to come back if you feel like you are up to the task")
    sys.exit()
else:
    print("Not a valid response!\nTry again!")
    sys.exit()

# Creates the player and enemy objects
def heal():
    increase = randint(20,45)
    hero.hp += increase
    print("You have gained %d hp, Your total hp is: %d" %(increase, hero.hp))

def getStats():
    player = ("%s: \n\tHP: %d\n\tAttack: %d\n\tDefense: %d\n\tgold: %d\n"
              %(hero.name, hero.hp, hero.attack, hero.defense, hero.gold))
    enemy = ("%s: \n\tHP: %d\n\tAttack: %d\n"
             %(introDrag.name, introDrag.hp, introDrag.attack))
    print (player + enemy)
    t.sleep(2)
def getPlayerStats():
    stats = ("%s: \n\tLevel: %d\n\tAttack: %d\n\tDefense: %d\n\tgold: %d\n\tLevel: %d\n\txp to next level: %d"
              % (hero.name, hero.level, hero.attack, hero.defense, hero.gold, hero.level, (hero.max_xp - hero.xp)))
    print(stats)
# Turn Loop
def battleDragon():
    while introDrag.hp > 0:
        t.sleep(3)
        choice = raw_input(battleMenu)
        if choice == "1":
            hero.attack_enemy(introDrag)
        elif choice == "2":
            heal()
        elif choice == "3":
            getStats()
        elif choice == "4":
            print("You have taken the cowards way out!\nTry again later if you feel brave!")
            hero.hp = 0
        else:
            print("Not a valid choice")

        t.sleep(2)
        # Dragon attacks if it is not dead and you did not choose to view the stats page or surrender the fight
        if not choice == '3' and introDrag:
            dragonDamage = randint(1,2)
            hero.hp -= dragonDamage
            print("\n\n\nThe dragon has attacked you for %d hp\n%s's current hp: %d\n"
                  %(dragonDamage, hero.name, hero.hp))

    # Winning or losing message
    if introDrag.hp <= 0:
        print("Congratulations! you have beaten the monster")
        hero.reward()
    else:
        print("Sorry you have been killed please try again")

    introDrag.hp = introDrag.maxhp

    t.sleep(4)
battleDragon()

# Brings user to the main menu
while True:
    choice = raw_input(mainMenu)
    # Battle
    if choice == '1':
        # Shop
        battleDragon()
    elif choice == '2':
        print("Hello World")
    elif choice == '3':
        getPlayerStats()
        t.sleep(5)
    elif choice == 4:
        print("Hello World")





