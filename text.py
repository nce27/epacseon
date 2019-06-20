def welcome():
  print("""
  #################################################
                 Welcome to Epacseon
  #################################################
                       ·Play·
                       ·Rules·
                       ·Quit·""")

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




'''
  if input.actions() =="t":
      print ("You took the item.")
'''

def Room2():
# NO items in this room [Starting room]
  print("""
  Room2
  You are standing in a near pitch-black dungeon which
  disappears into gloom to the east and west.
  Find the correct items to escape...

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

def Room3():
# A torch can be found here
  print("""
  Room3
  You follow the path to the east and see a bright light in the distance.
  You head towards the light, into Room 3... """)
  option = input("Do you want to pick up the torch? Yes/No?")

  if option == "yes" :
      print("You picked up a torch")

  elif option == "no":
      print("You left the torch")


def Room4():
    # There is a mushrom in the room
    print("""
    Room4
    Your curiosity leads you to Room 4...""")
    option = input("Do you want to pick up the crystal?     Yes/No?")

    if option == "yes" :
        print("You picked up a crystal")

    elif option == "no":
        print("You left the crystal")

def Room5():
    # There are berries in this room
    print("""
    Room5
    You follow the path into Room 5...""")
    option = input("Do you want to pick up the berries?     Yes/No?")

    if option == "yes" :
        print("You picked up a berries")

    elif option == "no":
        print("You left the berries")

def Room6():
    # This room contains a ring
    print("""
    Room6
    You have now entered Room 6...""")
    option = input("Do you want to pick up the ring?     Yes/No?")

    if option == "yes" :
        print("You picked up a ring")

    elif option == "no":
        print("You left the ring")

def Room7():
    #There are no items in this room
    print("""
    Room7
    Your instincts lead you to Room 7...""")

def Room8():
    #There are NO items in this room
    print("""
    Room8
    Delving depper into the dungeon, you head into Room 8...""")

def Room9():
    #There is a mushroom in this room
    print("""
    Room9
    Beginning to feel lost in this dungeon you wander into Room 9...
    """)
    option = input("Do you want to pick up the mushroom?    Yes/No?")

    if option == "yes" :
        print("You picked up a mushroom")

    elif option == "no":
        print("You left the mushroom")


def Room10():
    #The drink item can be found here
    print("""Room10
    Mysterious noises lead you into Room 10...""")

def Room11():
    # Need the crystal and the key to open the room
    print("""
    Room11
    Desperately searching for a way out, you follow the path into Room 11...""")

def Room12():
    #Room holds a key
    print("""
    Room12
    You follow the path to Room 12...""")

def Room13():
        #Final room
    print("""
    Room13
    You win""")

#Inventory class that holds user items.
'''
class ClassName(object):

    def __init__(mushroom,crystal):
        super(, self).__init__()
        self.arg = arg
         Inventory

'''


def noway():
    print ("You cannot go this way")
