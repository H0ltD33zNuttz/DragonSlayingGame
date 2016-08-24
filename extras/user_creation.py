# prompts the user with questions to get their character set up.
from cmdDragon import hero
import sys
import time


welcomeString = """Welcome to the game %s! \nThe objective of the game is to slay the dragon.
    """ % hero.name
print (welcomeString)
time.sleep(3)

itemString = ("We have started you off with a sword known as the \"Newb Sword\","
                  "as well as 3 potions!\nUse them wisely")
time.sleep(3)
# Confirms that the user actually wants to continue
confirmation = raw_input("\nDo you believe that you are up to the task?(yes or no) ")
time.sleep(1)
if confirmation == 'yes':
    print("Sounds great! Let's get started!")
elif confirmation == 'no':
    print("Alright, be sure to come back if you feel like you are up to the task")
    sys.exit()
else:
    print ("Not a valid response!\nTry again!")
    sys.exit()