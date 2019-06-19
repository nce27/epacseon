import os
import text

def run_game():
    start_menu()

def start_menu():
    os.system('clear')
    text.welcome()
    start_options()



def start_options():
  choice = input("> ")
  if choice.lower() == "play":
    play()
  elif choice.lower() == "rules":
    rules(start_options)
  elif choice.lower() == "quit":
    quit()
  else:
    idk(start_options)


def play():
  text.alley()
  alley_start()


def rules(cont_func):
    os.system('clear')
    text.rules()
    cont_func()




def quit():
  print("You may yet live to see another day.")

def idk(cont_func):
  print("I don't know what that means...")
  cont_func()




#This is the first room (2)
def alley_start():
  choice = input("> ")
  if choice.lower() == "n":
    dungeon()
  elif choice.lower() == "north":
    dungeon()
  elif choice.lower() == "s":
    Room5()
  elif choice.lower() == "south":
    Room5()
  elif choice.lower() == "w":
    Room2()
  elif choice.lower() == "west":
    Room2()
  elif choice.lower() == "e":
    Room3()
  elif choice.lower() == "east":
    Room3()
  elif choice.lower() == "quit":
    quit()
  elif choice.lower() == "rules":
    rules(play)
  else:
    idk(alley_start)





def dungeon():
  text.dungeon()
  choice = input("> ")
  if choice.lower() == "s":
    play()
  elif choice.lower() == "south":
    play()
  elif choice.lower() == "quit":
    quit()
  elif choice.lower() == "rules":
    rules(dungeon)
  else:
    idk(dungeon)





def Room2():

  text.Room2()
  choice = input("> ")
if choice.lower() == "e":
    alley_start()
elif choice.lower() == "east":
    alley_start()
elif choice.lower() == "s":
    Room4()
elif choice.lower() == "south":
    Room4()
elif choice.lower() == "w":
    noway()
elif choice.lower() == "west":
    noway()
elif choice.lower() == "n":
    Room2()
elif choice.lower() == "north":
    Room2()
elif choice.lower() == "quit":
    quit()
elif choice.lower() == "rules":
    rules(play)
else:
    idk(Room2)


'''
  text.Room2()
  choice = input("> ")
if choice.lower() == "e":
  dungeon()
elif choice.lower() == "east":
  dungeon()
elif choice.lower() == "n":
   dungeon()
elif choice.lower() == "north":
   dungeon()
elif choice.lower() == "s":
    dungeon()
elif choice.lower() == "south":
    dungeon()
elif choice.lower() == "w":
    play()
elif choice.lower() == "west":
    play()
elif choice.lower() == "quit":
    quit()
elif choice.lower() == "rules":
    rules(Room2)
else:
    idk(Room2)
'''


def Room3():
  text.Room3()
  choice = input("> ")
  if choice.lower() == "w":
    play()
  elif choice.lower() == "west":
    play()
  elif choice.lower() == "quit":
    quit()
  elif choice.lower() == "rules":
    rules(Room3)




#For holding/using/dropping items
def actions():
    actions = input("> ")
    if actions.lower() == "t":
      dungeon()
    elif actions.lower() == "take":
      dungeon()

    if actions.lower() == "u":
      dungeon()
    elif choice.lower() == "use":
      dungeon()

      if actions.lower() == "d":
        dungeon()
    elif actions.lower() == "drop":
        dungeon()



def items():
    torch.east_alley()
    if input.actions() == "t":
        print ("You took the torch.")
    elif input.actions() ==  "d":
        print ("You dropped the torch.")
    elif input.actions() == "u":
        print ("You used the torch. The room is brighter.")

    mushroom.east_alley()
    if input.actions() == "t":
        print ("You took the mushroom.")
    elif input.actions() ==  "d":
        print ("You dropped the mushroom.")
    elif input.actions() == "u":
        print ("You used the mushroom.")

    key.east_alley()
    if input.actions() == "t":
        print ("You took the key.")
    elif input.actions() ==  "d":
        print ("You dropped the key.")
    elif input.actions() == "u":
        print ("You used the key.")

    ring.east_alley()
    if input.actions() == "t":
        print ("You took the ring.")
    elif input.actions() ==  "d":
        print ("You dropped the ring.")
    elif input.actions() == "u":
        print ("You used the ring.")

    crystal.east_alley()
    if input.actions() == "t":
        print ("You took the crystal.")
    elif input.actions() ==  "d":
        print ("You dropped the crystal.")
    elif input.actions() == "u":
        print ("You used the crystal.")

    berries.east_alley()
    if input.actions() == "t":
        print ("You took the berries.")
    elif input.actions() ==  "d":
        print ("You dropped the berries.")
    elif input.actions() == "u":
        print ("You used the berries.")

    drink.east_alley()
    if input.actions() == "t":
        print ("You took the drink.")
    elif input.actions() ==  "d":
        print ("You dropped the drink.")
    elif input.actions() == "u":
        print ("You used the drink.")


def noway(cont_func):
  print("There is nothing in that direction.")
  cont_func()
