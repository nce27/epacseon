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
  text.Room2()
  Room2()


def rules(cont_func):
    os.system('clear')
    text.rules()
    cont_func()




def quit():
  print("You may yet live to see another day.")

def idk(cont_func):
  print("I don't know what that means...")
  cont_func()




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




def Room1():
 text.Room1()
 choice = input("> ")
 if choice.lower() == "e":
    Room2()
 elif choice.lower() == "east":
    Room2()
 elif choice.lower() == "s":
    Room4()
 elif choice.lower() == "south":
    Room4()
 elif choice.lower() == "w":
    noway()
 elif choice.lower() == "west":
    noway()
 elif choice.lower() == "n":
    dungeon()
 elif choice.lower() == "north":
    dungeon()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room1)

#This is the starting room
def Room2():
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
    Room1()
  elif choice.lower() == "west":
    Room1()
  elif choice.lower() == "e":
    Room3()
  elif choice.lower() == "east":
    Room3()
  elif choice.lower() == "quit":
    quit()
  elif choice.lower() == "rules":
    rules(play)
  else:
    idk(Room2)




def Room3():
 text.Room3()
 choice = input("> ")
 if choice.lower() == "e":
    noway()
 elif choice.lower() == "east":
    noway()
 elif choice.lower() == "s":
    Room6()
 elif choice.lower() == "south":
    Room6()
 elif choice.lower() == "w":
    Room2()
 elif choice.lower() == "west":
    Room2()
 elif choice.lower() == "n":
    dungeon()
 elif choice.lower() == "north":
    dungeon()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room3)

def Room4():
 text.Room4()
 choice = input("> ")
 if choice.lower() == "e":
    Room5()
 elif choice.lower() == "east":
    Room5()
 elif choice.lower() == "s":
    Room7()
 elif choice.lower() == "south":
    Room7()
 elif choice.lower() == "w":
    noway()
 elif choice.lower() == "west":
    noway()
 elif choice.lower() == "n":
    Room1()
 elif choice.lower() == "north":
    Room1()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room4)

def Room5():
 text.Room5()
 choice = input("> ")
 if choice.lower() == "e":
    Room6()
 elif choice.lower() == "east":
    Room6()
 elif choice.lower() == "s":
    Room8()
 elif choice.lower() == "south":
    Room8()
 elif choice.lower() == "w":
    Room4()
 elif choice.lower() == "west":
    Room4()
 elif choice.lower() == "n":
    Room2()
 elif choice.lower() == "north":
    Room2()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room5)

def Room6():
 text.Room6()
 choice = input("> ")
 if choice.lower() == "e":
    noway()
 elif choice.lower() == "east":
    noway()
 elif choice.lower() == "s":
    Room9()
 elif choice.lower() == "south":
    Room9()
 elif choice.lower() == "w":
    Room5()
 elif choice.lower() == "west":
    Room5()
 elif choice.lower() == "n":
    Room3()
 elif choice.lower() == "north":
    Room3()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room6)

def Room7():
 text.Room7()
 choice = input("> ")
 if choice.lower() == "e":
    Room8()
 elif choice.lower() == "east":
    Room8()
 elif choice.lower() == "s":
    Room10()
 elif choice.lower() == "south":
    Room10()
 elif choice.lower() == "w":
    noway()
 elif choice.lower() == "west":
    noway()
 elif choice.lower() == "n":
    Room4()
 elif choice.lower() == "north":
    Room4()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room7)

def Room8():
 text.Room8()
 choice = input("> ")
 if choice.lower() == "e":
    Room9()
 elif choice.lower() == "east":
    Room9()
 elif choice.lower() == "s":
    Room11()
 elif choice.lower() == "south":
    Room11()
 elif choice.lower() == "w":
    Room7()
 elif choice.lower() == "west":
    Room7()
 elif choice.lower() == "n":
    Room5()
 elif choice.lower() == "north":
    Room5()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room8)

def Room9():
 text.Room9()
 #items.Crystal()
 choice = input("> ")
 if choice.lower() == "e":
    noway()
 elif choice.lower() == "east":
    noway()
 elif choice.lower() == "s":
    Room12()
 elif choice.lower() == "south":
    Room12()
 elif choice.lower() == "w":
    Room8()
 elif choice.lower() == "west":
    Room8()
 elif choice.lower() == "n":
    Room6()
 elif choice.lower() == "north":
    Room6()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room9)

def Room10():
 text.Room10()
 choice = input("> ")
 if choice.lower() == "e":
    Room11()
 elif choice.lower() == "east":
    Room11()
 elif choice.lower() == "s":
    noway()
 elif choice.lower() == "south":
    noway()
 elif choice.lower() == "w":
    dungeon()
 elif choice.lower() == "west":
    dungeon()
 elif choice.lower() == "n":
    Room7()
 elif choice.lower() == "north":
    Room7()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room10)

def Room11():
 text.Room11()
 choice = input("> ")
 if choice.lower() == "e":
    Room12()
 elif choice.lower() == "east":
    Room12()
 elif choice.lower() == "s":
    noway()
 elif choice.lower() == "south":
    noway()
 elif choice.lower() == "w":
    Room10()
 elif choice.lower() == "west":
    Room10()
 elif choice.lower() == "n":
    Room8()
 elif choice.lower() == "north":
    Room8()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room11)

def Room12():
 text.Room12()
 choice = input("> ")
 if choice.lower() == "e":
    dungeon()
 elif choice.lower() == "east":
    dungeon()
 elif choice.lower() == "s":
    noway()
 elif choice.lower() == "south":
    noway()
 elif choice.lower() == "w":
    Room11()
 elif choice.lower() == "west":
    Room11()
 elif choice.lower() == "n":
    Room9()
 elif choice.lower() == "north":
    Room9()
 elif choice.lower() == "quit":
    quit()
 elif choice.lower() == "rules":
    rules(play)
 else:
    idk(Room12)



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


'''
class items():
    def torch(Room3):
        \
    if input.actions() == "t":
        print ("You took the torch.") \
    elif input.actions() ==  "d":
        print ("You dropped the torch.") \
    elif input.actions() == "u":
        print ("You used the torch. The room is brighter.")

    def mushroom.Room9(items)
    if input.actions() == "t":
        print ("You took the mushroom.")
    elif input.actions() ==  "d":
        print ("You dropped the mushroom.")
    elif input.actions() == "u":
        print ("You used the mushroom.")

    def key.Room12(items)
    if input.actions() == "t":
        print ("You took the key.")\
    elif input.actions() ==  "d":
        print ("You dropped the key.")\
    elif input.actions() == "u":
        print ("You used the key.")

def ring.Room6()
    if input.actions() == "t":
        print ("You took the ring.")\
    elif input.actions() ==  "d":
        print ("You dropped the ring.")\
    elif input.actions() == "u":
        print ("You used the ring.")

    def crystal.Room4()
    if input.actions() == "t":
        print ("You took the crystal.")
    elif input.actions() ==  "d":
        print ("You dropped the crystal.")
    elif input.actions() == "u":
        print ("You used the crystal.")

    def berries.Room5()
    if input.actions() == "t":
        print ("You took the berries.")
    elif input.actions() ==  "d":
        print ("You dropped the berries.")
    elif input.actions() == "u":
        print ("You used the berries.")

    def drink.Room10()
    if input.actions() == "t":
        print ("You took the drink.")
    elif input.actions() ==  "d":
        print ("You dropped the drink.")
    elif input.actions() == "u":
        print ("You used the drink.")

'''


def noway(cont_func):
  print("There is nothing in that direction.")
  cont_func()
