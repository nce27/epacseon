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

def alley():
  print("""
  You are standing in a near pitch-black dungeon which
  disappears into gloom to the east and west. Which way do you go?
  """)

def dungeon():
  print("""
  The door is closed behind you you cannot go this way""")

def Room2():
    # This allows movement for the west + __ option
    # NO items in this room
  print( """
  You follow the path to the west. You feel the ground tilt
  downhill...""")

def Room3():
# This allows movement for the west + __ option
# Torch can be found here
  print("""
  You follow the path to the east and see a bright light in the distance.
  You head towards the light and find a torch. """)

def Room4():
    # This allows movement for the west + __ option
    # There is a mushrom in the room
    print("""
    Heading into the next area you come across a mushroom ...""")

def Room5():
      print("""
      You follow the path to the east...""")

def Room6():
    #This allows movement for the west + __ option
    print("""
    You follow the path to the east...""")

def Room7():
    #This allows movement for the west + __ option
    print("""
    You follow the path to the east...""")

def Room8():
    #This allows movement for the west + __ option
    print("""
    You follow the path to the east...""")

def Room9():
    #This allows movement for the west + __ option
    print("""
    You follow the path to the east...""")

def Room10():
    #This allows movement for the __ + __ option
    #The drink item can be found here
    print("""
    You follow the path to the east...""")

def Room11():
    #This allows movement for the west + __ option
    #This is the boss room (Need the crystal and the key)
    print("""
    You follow the path to the east...""")

def Room12():
    #This allows movement for the west + __ option
    #Berries in this room
    print("""
    You follow the path to the east...""")
