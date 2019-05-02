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
  This is a complex world but I am a simple guide.
  I can understand short commands of 1 or 2 words,)
  so choose wisely.
  You can move through this world with a compass:
    'north' or 'n' will move you forwards,
    'south' or 's' will move you backwards,
    'west' or 'w' will move you left,
    'east' or 'e' will move you right,
  Occasionally there will be chances to explore to
  the 'ne', 'nw', 'se', or 'sw'.
  I will make these chances known to you.

  You can examine your surroundings or objects with
    'examine' or 'e', or 'look' or 'l'.

  Other commands include:
    'use', 'take', 'drop', and 'list'.

  You can see these instructions again at any time.

  #################################################""")

def alley():
  print("""
  You are standing in a near pitch-black alley which
  disappears into the gloom to the east and west.
  Before you is house with boarded up windows and one
  door.""")

def house():
  print("""
  The door creaks as you push through. When it closes
  behind you, the darkness is complete.""")

def west_alley():
  print( """
  You follow the alley to the west. You feel the ground tilt
  downhill.
  The alley stretches before you and back to the east...""")

def east_alley():
  print("""
  You follow the alley to the east. It seems to be getting
  lighter as you go.
  The alley stretches before you and back to the west...""")
