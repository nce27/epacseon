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

def alley_start():
  choice = input("> ")
  if choice.lower() == "n":
    house()
  elif choice.lower() == "north":
    house()
  elif choice.lower() == "s":
    noway(alley_start)
  elif choice.lower() == "south":
    noway(alley_start)
  elif choice.lower() == "w":
    west_alley()
  elif choice.lower() == "west":
    west_alley()
  elif choice.lower() == "e":
    east_alley()
  elif choice.lower() == "east":
    east_alley()
  elif choice.lower() == "quit":
    quit()
  elif choice.lower() == "rules":
    rules(play)
  else:
    idk(alley_start)

def house():
  text.house()
  choice = input("> ")
  if choice.lower() == "s":
    play()
  elif choice.lower() == "south":
    play()
  elif choice.lower() == "quit":
    quit()
  elif choice.lower() == "rules":
    rules(house)
  else:
    idk(house)

def west_alley():
  text.west_alley()
  choice = input("> ")
  if choice.lower() == "e":
    play()
  elif choice.lower() == "east":
    play()
  elif choice.lower() == "quit":
    quit()
  elif choice.lower() == "rules":
    rules(west_alley)

def east_alley():
  text.east_alley()
  choice = input("> ")
  if choice.lower() == "w":
    play()
  elif choice.lower() == "west":
    play()
  elif choice.lower() == "quit":
    quit()
  elif choice.lower() == "rules":
    rules(east_alley)

def noway(cont_func):
  print("There is nothing in that direction.")
  cont_func()
