from __future__ import print_function
from .items import newbSword
from random import randint as rnd
from time import sleep

class Player:
    def __init__(self):
        self.name = raw_input("What is your name? " )
        self.gold = 0
        self.level = 1
        self.xp = 0
        self.max_xp = 10
        self.hp = 150 * (self.level * .5)
        self.maxHealth = 150 * (self.level * .5)
        self.attack = 1 * self.level
        self.defense = 1 * self.level

    def levelUp(self):
        print("Hello World")

    # Awards experience to the player based on the experience and stats of the enemy.
    def reward(self):
        xpreward = self.level * 8 + self.attack + self.defense
        hero.xp += xpreward
        print("\nCongratulations! you have defeated the monster and gained %d experience." %xpreward)
        if hero.xp >= hero.max_xp:
            self.level += 1
            self.attack *= 2
            self.defense *= 2
            self.hp *= 1.5
            self.max_xp *= 1.5
            self.xp = 0
            print("Congratulations! You are now level %d" % self.level)

            hero.max_xp += self.level * 2 + 18
    def attack_enemy(self, enemy):
        rand_bonus = rnd(1,4)
        damage = hero.attack * newbSword.attack * rand_bonus
        enemy.hp -= damage
        if enemy.hp <= 0:
            print("Congratulations! You have killed the enemy!")
        if rand_bonus <= 3 and enemy.hp >= 0:
            print("You have struck the enemy for %d hp." % damage)
        else:
            print("Wow! You have dealt a critical strike for %d hp!" % damage)
        print("Leaving them with %d hp" % enemy.hp)

        if enemy.hp <= 0:
            hero.reward()


# Dragon Stats
class Dragon:
    def __init__(self, name, attack, defense, hp, maxhp, level):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.maxhp = maxhp
        self.level = level
hero = Player()
introDrag = Dragon('Intro Dragon', 1, 1, 35, 35, 1)