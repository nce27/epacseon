def welcome():
  print("""
  #################################################
                 Welcome to Epacseon
  #################################################
                       ·Play·
                       ·Rules·
                       ·Quit·""")
import os
import text

def run_game():
    start_menu()
def start_menu():
    os.system('clear')
    text.welcome()


Inventory = ["Rock"]

def rules():
  print("""
  #################################################
  You are in a dungeon and are looking for items to escape.
  Some of the items will be useful to escape the dungeon,
   whereas some will result in death.
  I can understand short commands of 1 or 2 words,)
  so choose wisely.

  You can move through this world with a compass:
    'north' or 'n' will move you forwards,
    'south' or 's' will move you backwards,
    'west' or 'w' will move you left,
    'east' or 'e' will move you right,

  Commands for items include:
    'use','take' and 'drop'.

  You can see these instructions again at any time.

  #################################################""")


def Room2():
# NO items in this room [Starting room]
  print("""
  Room2
  You are standing in a near pitch-black dungeon which
  disappears into gloom to the east and west.

  Find the correct items to escape...

  All you have in your inventory is a rock

  Which way do you go?
  """)

def dungeon():
  print("""
  The door is closed behind you you cannot go this way""")

def Room1():
  print( """
  Room1
  You follow the path to the west. You feel the ground tilt
  downhill into Room 1...""")
  print("Your inventory:")
  print (Inventory)

def Room3():
# A torch can be found here
    print("""
    Room3
    You follow the path to the east and see a bright light in the distance.
    You head towards the light, into Room 3... """)
    option = input("Do you want to pick up the torch? Yes/No?   ")
    print("Your inventory:")
    print (Inventory)

    if option == "yes" :
      print( "You picked up a torch")
      Inventory.append("Torch") #Attempt to add to the inventory
      print(Inventory)

    if option == "no":
        print("You left the torch")
        print (Inventory)

def Room4():
    # There is a mushrom in the room
    print("""
    Room4
    Your curiosity leads you to Room 4 self...""")
    option = input("Do you want to pick up the crystal?     Yes/No? ")
    print("Your inventory:")
    print (Inventory)

    if option == "yes" :
        print("You picked up a crystal")
        Inventory.append("Crystal") #Attempt to add to the inventory
        print(Inventory)

    elif option == "no":
        print("You left the crystal")
        print(Inventory)



def Room5():
    # There are berries in this room
    print("""
    Room5
    You follow the path into Room 5...""")
    option = input("Do you want to pick up the berries?     Yes/No? ")
    print("Your inventory:")
    print (Inventory)

    if option == "yes" :
        print("You picked up the berries but they were poisonous. You died...")
#Causes the user to start again if they pick yes
        start_menu()
        os.system('clear')
        print("You picked up the berries but they were poisonous. You died...")
        text.welcome()

    elif option == "no":
        print("You left the berries")
        print (Inventory)



def Room6():
    # This room contains a ring
    print("""
    Room6
    You have now entered Room 6...""")
    option = input("Do you want to pick up the ring?     Yes/No?    ")
    print("Your inventory:")
    print (Inventory)

    if option == "yes" :
        print("You picked up a ring")
        Inventory.append("ring") #Attempt to add to the inventory
        print(Inventory)

    elif option == "no":
        print("You left the ring")
        print (Inventory)



def Room7():
    #There are no items in this room
    print("""
    Room7
    Your instincts lead you to Room 7...""")

    print("Your inventory:")

    print (Inventory)


def Room8():
    #There are NO items in this room
    print("""
    Room8
    Delving depper into the dungeon, you head into Room 8...""")
    print("Your inventory:")

    print (Inventory)


def Room9():
    #There is a mushroom in this room
    print("""
    Room9
    Beginning to feel lost in this dungeon you wander into Room 9...
    """)
    print("Your inventory:")

    print (Inventory)

    option = input("Do you want to pick up the mushroom?    Yes/No? ")


    if option == "yes" :
        print("You picked up a mushroom...Oh no! It was poisonous...you died.")
#Causes the user to start again if they pick yes
        start_menu()
        os.system('clear')
        text.welcome()

    elif option == "no":
        print("You left the mushroom")


def Room10():
    #The drink item can be found here
    print("""Room10
    Mysterious noises lead you into Room 10...""")

    print("Your inventory:")

    print (Inventory)

    option = input("Do you want to pick up the drink?    Yes/No?    ")

    if option == "yes" :
        print("You picked up the drink")
        start_menu()
        os.system('clear')
        print("You drank the drink but it was radioactive. You died...")
        text.welcome()

    elif option == "no":
        print("You left the drink")
        print (Inventory)


def Room11():
    # Need the key to open the room
    print("""
    Room11
    Desperately searching for a way out, you follow the path into Room 11...""")

    if "key" in Inventory:
        print("You have unlocked the door into room 13")

def Room12():
    #Room holds a key
    print("""
    Room12
    You follow the path to Room 12...""")

    print("Your inventory:")

    print (Inventory)

    option = input("Do you want to pick up the key?    Yes/No?  ")

def Room13():
#Final room - check to see whether the items required to pass are present in Inventory

    print("Room13")
    if "crystal" in Inventory:
        print("""
        Room13
        ou have escaped! You may live to see another day...""")


def noway():
    print ("You cannot go this way")
