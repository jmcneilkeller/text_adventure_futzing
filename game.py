## Intern: The Game

import random
import cmd
from textwrap import dedent
import sys
import os
import time
from random import uniform

screen_width = 100

#### Player Setup ####

class Player():
    
    def __init__(self):
        # Player class.
        self.name = ""
        self.will = 100
        self.solves = 0
        self.location = 'c2'
        self.gameover = False

        
myPlayer = Player()
        
#### Typewriter ####

def typewriter(text, start=None, stop=None):
    # Prints out in a typewriter effect.
    # Expects a string
    if start is None:
        start = 0.025
    if stop is None:
        stop = 0.1
    for i in range(len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(uniform(start, stop))

#### Title Screen ####

def title_screen():
    os.system('clear')
    print(dedent("""
                    #############################
                    ##### Intern: The Game ######
                    #############################
                              |PLAY|    
                              |HELP|
                              |QUIT|             """))
    title_screen_selection()

def title_screen_selection():
    option = input('> ')
    if option.lower() == ('play'):
        setup_game()
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print('Please choose an option.')
        option = input('> ')
        if option.lower() == ('play'):
            setup_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()
    
def help_menu():
    print(dedent("""
             Your goal will be to have a conversation with your boss 
             before you lose the will to live.
             
             Your interactions with your co-workers and the office can either 
             increase or decrease your will to live.
             
             If your will to live reaches zero, then...              
                           
                         #############################
                         #         CONTROLS          #
                         #############################
    
             - Valid actions are move, look, talk, location, open or quit.
                           """))
    print("Would you like to play or quit?")
    title_screen_selection()

def setup_game():
    os.system('clear')

    # NAME
    typewriter("A wizened old man approaches you.\n")
    question1 = "What is your name, traveler?"
    typewriter(question1)
    player_name = input("\n> ")
    while not player_name:
        print("Come now, you have a name.")
        typewriter(question1)
        player_name = input("\n> ")
        if player_name:
            player_name = myPlayer.name
            break

    # DEGREE FAKE OUT
    question2 = "\nVery good! Yes, very good.\nAnd what kind of degree do you have, " + player_name + "?"
    typewriter(question2)
    degree = input("\n> ")
    while not degree:
        typewriter("Surely you went to college.")
        typewriter("What was your degree?")
        degree = input("\n> ")

    soulcrush1 = "\n" + degree + ", eh? Well, that's pretty useless here.\n"
    soulcrush2 = "You're an intern now...\n"
    soulcrush3 = dedent(""" 
                           ** Thunder flashes and lightning crackles **
                                   The old man disappears...
                        """)
    
    typewriter(soulcrush1)
    typewriter(soulcrush2)
    typewriter(soulcrush3)
    time.sleep(2)

    os.system('clear')

    # INTRODUCTION #
    print("                  #### GAME START ####")
    time.sleep(0.5)
    introduction = dedent("""             
               'Welcome to Synergistic Conglomerates International!
               
               Congratulations on being accepted for our fall internship!
               You were the most accomplished applicant to also have 
               passed a drug screening! 
               
               This will be your office. If you need anything, just let
               me know. My office is on a floor you don't have access to,
               but feel free to give me a jingle, hokay!?'
               
               You start to ask if there was just a wizened old man there,
               but she's already closed the door behind her.
               
               """)
    typewriter(introduction,0.0001)
    main_game()

### GAME INTERACTIVITY ###

# Add specific "battle" prompt functionality.


def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location + ' #')
    print('# ' + worldmap[myPlayer.location]["ZONENAME"] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def world_prompt():
    print("\n" + "====================")
    print("What would you like to do?\n")
    print("move, look, talk, location, open or quit?\n")
    action = input("> ")
    valid_actions = ["move", "quit", "look", "talk", "open", "location"]
    while action.lower() not in valid_actions:
        print("Invalid command. Try again friend.")
        action = input("> ")
    if action.lower().strip() == "quit":
        sys.exit()
    elif action.lower().strip() == "move":
        move(action.lower())
    elif action.lower().strip() == "look":
        look(action.lower())
    elif action.lower().strip() == "talk":
        battle_prompt()
    elif action.lower().strip() == "open":
        open_it(action.lower())
    elif action.lower().strip() == "location":
        print_location()

def battle_prompt():
    if worldmap[myPlayer.location]["SOLVED"]:
        print("Do you really want to have this conversation again?")
    elif worldmap[myPlayer.location]["PERSON"] == "ITGuy":
        itguy()
    elif



def move(action):
    print("\n" + "====================")
    print("\nOk, let's meander around the office!\n"
          "Which way would you like to " + action + "?\n")
    dest = input("> ")
    if dest.lower() == 'up':
        destination = worldmap[myPlayer.location]["UP"]
        print_location()
        movement(destination)
    elif dest.lower() == 'down':
        destination = worldmap[myPlayer.location]["DOWN"]
        movement(destination)
    elif dest.lower() == 'left':
        destination = worldmap[myPlayer.location]["LEFT"]
        movement(destination)
    elif dest.lower() == 'right':
        destination = worldmap[myPlayer.location]["RIGHT"]
        movement(destination)

def movement(destination):
    print("\nYou have moved to " + worldmap[destination]["ZONENAME"] + ".")
    myPlayer.location = destination
    print_location()

def look(action):
    if worldmap[myPlayer.location]["SOLVED"]:
        print("You've already seen whatever can be seen.")
    else:
        print(dedent(worldmap[myPlayer.location]["DESCRIPTION"]))

def open_it():
    if worldmap[myPlayer.location]["SOLVED"]:
        print("You've already ransacked the place.")
    else:
        pass


    
### GAME FUNCTIONALITY ###

def main_game():
    while myPlayer.gameover is False:
        world_prompt()
        # Here handle boss defeated, puzzles solves, etc...


#### Scenarios ####

def itguy():
    typewriter("You say hello.")
    typewriter(""""..."""")
    print("Would you like to flirt, ")
    action = input("> ")


def prick():
    if
    pass

def receptionist():
    pass

def boss():
    pass

def vaxxer():
    pass

def hottie():
    pass

def printer():
    pass

def conference_room():
    pass

def kitchen():
    pass





### MAP ###
### Start in C2.###
"""
   A       B      C
------------------------
| BOSS | Recept| Conf  | 1
------------------------
|      | Prick | START | 2
------------------------ 
| Kitch|  Vax  | Hot   | 3
------------------------
|      | Print | IT    | 4
------------------------
"""


ZONENAME = ""
DESCRIPTION = "description"
LOOK = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solved_places = {"a1": False, "a2": False, "a3": False, "a4": False,
                 "b1": False, "b2": False, "b3": False, "b4": False,
                 "c1": False, "c2": False, "c3": False, "c4": False,
                 }
    
worldmap = {"a1": {
                   "ZONENAME": "Boss's office",
                   "DESCRIPTION": 'description',
                   "LOOK": 'examine',
                   "OPEN": "opened",
                   "SOLVED": False,
                   "UP": "",
                   "DOWN": "a2",
                   "LEFT": "",
                   "RIGHT": "b1",
                  },
            "a2": {
                   "ZONENAME": "",
                   "DESCRIPTION": "description",
                   "LOOK": 'examine',
                   "OPEN": "opened",
                   "SOLVED": False,
                   "UP": "a1",
                   "DOWN": "a3",
                   "LEFT": "",
                   "RIGHT": "b2",
                  },
            "a3": {
                    "ZONENAME": "Kitchen",
                    "DESCRIPTION": 'description',
                    "LOOK": "examine",
                    "OPEN": "opened",
                    "SOLVED": False,
                    "UP": "a2",
                    "DOWN": "a4",
                    "LEFT": "",
                    "RIGHT": "b3",
                   },
            "a4": {
                    "ZONENAME": "",
                    "DESCRIPTION": 'description',
                    "LOOK": 'examine',
                    "OPEN": "opened",
                    "SOLVED": False,
                    "UP": "a3",
                    "DOWN": "",
                    "LEFT": "",
                    "RIGHT": "b4",
                   },
            "b1": {
                   "ZONENAME": "",
                   "DESCRIPTION": 'description',
                   "LOOK": 'examine',
                   "OPEN": "opened",
                   "SOLVED": False,
                   "UP": "",
                   "DOWN": "b2",
                   "LEFT": "a1",
                   "RIGHT": "c1",
                  },
            "b2": {
                   "ZONENAME": "Sales lead's office",
                   "DESCRIPTION": "It's an office, baby.",
                   "LOOK": 'examine',
                   "OPEN": "opened",
                   "SOLVED": False,
                   "UP": "b1",
                   "DOWN": "b3",
                   "LEFT": "a2",
                   "RIGHT": "c2",
                  },
            "b3": {
                    "ZONENAME": "Financial Analyst's office",
                    "DESCRIPTION": 'description',
                    "LOOK": 'examine',
                    "OPEN": "opened",
                    "SOLVED": False,
                    "UP": "b2",
                    "DOWN": "b4",
                    "LEFT": "a3",
                    "RIGHT": "c3",
                   },
            "b4": {
                    "ZONENAME": "Printer room",
                    "DESCRIPTION": 'description',
                    "LOOK": 'examine',
                    "OPEN": "opened",
                    "SOLVED": False,
                    "UP": "b3",
                    "DOWN": "",
                    "LEFT": "a4",
                    "RIGHT": "c4",
                   },
            "c1": {
                   "ZONENAME": "Conference Room",
                   "DESCRIPTION": 'description',
                   "LOOK": 'examine',
                   "OPEN": "opened",
                   "SOLVED": False,
                   "UP": "",
                   "DOWN": "c2",
                   "LEFT": "b1",
                   "RIGHT": "",
                  },
            "c2": {
                   "ZONENAME": "startzone",
                   "DESCRIPTION": "A converted storage closet.",
                   "LOOK": 'examine',
                   "OPEN": "opened",
                   "SOLVED": False,
                   "UP": "c1",
                   "DOWN": "c3",
                   "LEFT": "b2",
                   "RIGHT": "",
                  },
            "c3": {
                    "ZONENAME": "",
                    "DESCRIPTION": 'description',
                    "LOOK": 'examine',
                    "OPEN": "opened",
                    "SOLVED": False,
                    "UP": "c2",
                    "DOWN": "c4",
                    "LEFT": "b3",
                    "RIGHT": "",
                   },
            "c4": {
                    "ZONENAME": "IT Room",
                    "DESCRIPTION": "The room is crowded with boxes of cables, broken servers and "
                                   "a sullen looking man staring at his computer screen",
                    "LOOK": 'examine',
                    "OPEN": "opened",
                    "SOLVED": False,
                    "UP": "c3",
                    "DOWN": "",
                    "LEFT": "b4",
                    "RIGHT": "",
                   }

}  






title_screen()
    
    
    
    
          
          
          
          
        