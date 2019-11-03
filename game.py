## Intern: The Game

import random
import cmd
from textwrap import dedent
import sys
import os
import time
from random import uniform

screen_width = 150

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

def will_check():
    print("You have " + str(myPlayer.will) + " will left.")
    world_prompt()

def quit():
    print("Goodbye!\n")
    sys.exit()
        
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
        quit()
    while option.lower() not in ['play','help','quit']:
        print('Please choose an option.')
        option = input('> ')
        if option.lower() == ('play'):
            setup_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            quit()
    
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

    # DEGREE FAKE OUT #### UNCOMMENT ONCE DEBUGGING IS COMPLETE. #####
    # question2 = "\nVery good! Yes, very good.\nAnd what kind of degree do you have, " + player_name + "?"
    # typewriter(question2)
    # degree = input("\n> ")
    # while not degree:
    #     typewriter("Surely you went to college.")
    #     typewriter("What was your degree?")
    #     degree = input("\n> ")
    #
    # soulcrush1 = "\n" + degree + ", eh? Well, that's pretty useless here.\n"
    # soulcrush2 = "You're an intern now...\n"
    # soulcrush3 = dedent("""
    #                        ** Thunder flashes and lightning crackles **
    #                                The old man disappears...
    #                     """)
    #
    # typewriter(soulcrush1)
    # typewriter(soulcrush2)
    # typewriter(soulcrush3)
    # time.sleep(2)

    os.system('clear')

    # INTRODUCTION #
    print("                  #### GAME START ####")
    time.sleep(0.5)
    ### UNCOMMENT ONCE TESTING IS DONE! ###
    # introduction = dedent("""
    #            'Welcome to Synergistic Conglomerates International!
    #
    #            Congratulations on being accepted for our fall internship!
    #            You were the most accomplished applicant to also have
    #            passed a drug screening!
    #
    #            This will be your office. If you need anything, just let
    #            me know. My office is on a floor you don't have access to,
    #            but feel free to give me a jingle, hokay!?'
    #
    #            You start to ask if there was just a wizened old man there,
    #            but she's already closed the door behind her.
    #
    #            """)
    # typewriter(introduction,0.0001)
    main_game()

### GAME INTERACTIVITY ###

# Add specific "battle" prompt functionality.

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location + ' #')
    print('# ' + worldmap[myPlayer.location][ZONENAME] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def world_prompt():
    print("\n" + "====================")
    print("What would you like to do?\n")
    print("move, look, talk, location, open or quit?\n")
    action = input("> ")
    valid_actions = ["move", "quit", "look", "talk", "open", "location", "will"]
    while action.lower().strip() not in valid_actions:
        print("Invalid command. Try again, friend.")
        action = input("> ")
    if action.lower().strip() == "quit":
        quit()
    elif action.lower().strip() == "move":
        move(action.lower())
    elif action.lower().strip() == "look":
        look(action.lower())
    elif action.lower().strip() == "talk":
        battle_prompt(myPlayer.location)
    elif action.lower().strip() == "open":
        open_it(myPlayer.location)
    elif action.lower().strip() == "location":
        print_location()
    elif action.lower().strip() == "will":
        will_check()


def move(action):
    print("\n" + "====================")
    print("\nOk, let's meander around the office!\n"
          "Which way would you like to " + action + "?\n")
    print("Up, down, left or right?")
    dest = input("> ")
    directions = ["up", "down", "left", "right"]
    while dest.lower().strip() not in directions:
        print("Nope, you can't move that way.")
        print("\nWhich way would you like to " + action + "?\n")
        dest = input("> ")
    if dest.lower().strip() == "up":
        destination = worldmap[myPlayer.location][UP]
        movement(destination)
    elif dest.lower().strip() == "down":
        destination = worldmap[myPlayer.location][DOWN]
        movement(destination)
    elif dest.lower().strip() == "left":
        destination = worldmap[myPlayer.location][LEFT]
        movement(destination)
    elif dest.lower().strip() == "right":
        destination = worldmap[myPlayer.location][RIGHT]
        movement(destination)

def movement(destination):
    print("\nYou have moved to " + worldmap[destination][ZONENAME] + ".")
    myPlayer.location = destination
    print_location()

def look(action):
    if worldmap[myPlayer.location][SOLVED]:
        print("You've already seen whatever can be seen.")
    else:
        print(worldmap[myPlayer.location][DESCRIPTION])

def gameover():
    myPlayer.gameover = True
    quit()


    
### GAME FUNCTIONALITY ###

def main_game():
    while myPlayer.gameover is False:
        world_prompt()
        # Here handle boss defeated, puzzles solves, etc...


#### Scenarios ####

def a1():
    # Boss scenario
    while not worldmap["b1"][SOLVED]:
        print("Your boss looks up. 'Who're you?'\n")
        print("Your boss doesn't know your name! Your will to live reduces to zero!\n")
        gameover()
    print("Successful test!")

def b1():
    # Receptionist scenario.
    if myPlayer.solves < 10:
        print("")
    print("Successful test!")

def b2():
    # Prick scenario
    if not worldmap['b4'][SOLVED]:
        print("")
    print("Successful test!")

def b3():
    # Anti-vaxxer scenario
    print("Successful test!")

def b4():
    # Printer scenario
    pass

def c1():
    if worldmap["c1"][SOLVED]:
        print("There is nothing more to do here.")
    pass

def c2():
    # Your "office"
    while not worldmap["c4"][SOLVED]:
        # MORE CODE HERE!!!
        world_prompt()
    if worldmap["c2"][SOLVED]:
        print("There is nothing more to do here.")

def c3():
    # Hottie scenario
    if worldmap["c3"][SOLVED]:
        print("There is nothing more to do here.")
    print("Successful test!")

def c4():
    # IT guy scenario.
    if worldmap["c4"][SOLVED]:
        print("There is nothing more to do here.")
    typewriter("You say hello.")
    typewriter("\n...no response\n")
    print(dedent("""Would you like to:
                 1. Clap your hands and say: 'Hey! I'm talking here!'
                 2. Introduce yourself.
                 3. Try to find something to say about the Star Trek poster on the wall.
                 Enter 1, 2 or 3.
                  """))
    action = input("> ")
    valid_actions = ["1","2","3"]
    while action not in valid_actions:
        print("Not an option.\nInput 1, 2 or 3.")
        action = input("> ")
    if action == "1":
        print("He sniffs and starts to type on his keyboard."
              "\nYour phone starts to beep loudly, then powers down abruptly. You can't get it back on."
              "\nYour will to live has decreased by 30 points. You are also kind of an asshole.")
        myPlayer.will -= 30
        world_prompt()
    elif action == "2":
        print("'....'")
        print(dedent("""Would you like to:
                     1. Introduce yourself again. 
                     2. Ask about your monitor. 
                     3. Stand in silence. 
                     Enter 1, 2 or 3.
                     """))
        action_2 = input("> ")
        while action_2 not in valid_actions:
            print("Not an option.\nInput 1, 2 or 3.")
            action_2 = input("> ")
        if action_2 == "1":
            print("'Yes, I know.', he says dismissively and puts his headphones on.")
            print("Your will to live decreases by 10 points.")
            myPlayer.will -= 10
            world_prompt()
        elif action_2 == "2":
            print("'Finally! Someone who gets to the point.'\n")
            print("'Every time someone comes to ask me for stuff, they just want to make small talk.'\n")
            print("'I'll have your monitor hooked up. It'll be ready by the time you get back to your room.'\n")
            myPlayer.will += 5
            print("\nYour live to live increases by 5 points.")
            worldmap["c4"][SOLVED] = True
            myPlayer.solves += 1
            world_prompt()
        elif action_2 == "3":
            print("'You're creeping me out, man', he says. He puts his headphones back on.")
            print("Your will to live decreases by 10 points.")
            myPlayer.will -= 10
            print(dedent("""What would you like to do:
                                 1. Keep standing there silently. 
                                 2. Leave. 
                                 Enter 1 or 2.
                                 """))
            action_3 = input("> ")
            while action_3 == "1":
                print("This is awkward.")
                print("Your will to live decreases by 10 points.")
                myPlayer.will -= 10
                print(dedent("""What would you like to do:
                                                 1. Keep standing there silently. 
                                                 2. Leave. 
                                                 Enter 1 or 2.
                                                 """))
                action_3 = input("> ")
            if action_3 == "2":
                world_prompt()
    elif action == "3":
        print(dedent("""He sniffs. 'What was the name of the Romulan captain Kirk does battle with
                 in the seminal episode Balance of Terror?'
                 Enter 1, 2 or 3:
                 1. Spock.
                 2. Fluttershy.
                 3. Saavak.
                 """))
        action_3 = input("> ")
        while action_3 not in valid_actions:
            print("Not an option.\nInput 1, 2 or 3.")
            action_3 = input("> ")
        if action_3 == "1":
            print("He shakes his head and puts his headphones on.")
            print("Your will to live decreases by 10 points.")
            myPlayer.will -= 10
            world_prompt()
        elif action_3 == "2":
            print("He looks at you with disgust, and puts his headphones on.")
            print("\nYour live decreases by 20 points.")
            myPlayer.will -= 20
            world_prompt()
        elif action_3 == "3":
            print("'Trick question. He is unnamed.' "
                  "\n He puts his headphones on and ignores you."
                  "\n Your will to live decreases by 10 points.")
            myPlayer.will -= 10
            world_prompt()

def conference_room():
    # Conference room scenario
    pass

def a3():
    # Kitchen scenario
    if worldmap[location][SOLVED]:
        print("The cabinet fixed itself. Spooky.")
    typewriter("It's the kitchen. It has the usual assortment of cheap tea.\n You notice one of the cabinet doors is swinging open.\n")
    print(dedent("""What would you like to do?:"
                 "1. Try to close it."
                 "2. Just leave it.
                 Enter 1 or 2."""))
    action = input("> ")
    if action == "1":
        print("You push it closed. It clicks open again.\n")
        print(dedent("""What do you want to do?:"
                     "1. Try to close it again."
                     "2. Just leave it.
                     Enter 1 or 2."""))
        action_2 = input("> ")
        if action_2 == 1:
            print(dedent("""You shut it closed with a bit more force and start to walk away.
                         You hear a click as it springs back open."""))
        elif action_2 == 2:
            world_prompt()
    elif action == "2":
        world_prompt()

battle_dict = {"a1": a1, "b1": b1, "b2": b2, "b3": b3,
             "c3": c3, "c4": c4}

def battle_prompt(location):
    if worldmap[location][SOLVED]:
        print("Do you really want to have this conversation again?")
        world_prompt()
    elif location in ["c1","a3","b4"]:
        print("Ummm...there is no one in the room. Who are you talking to?")
        myPlayer.will -= 5
        print("Your will to live has decreased by five points.")
        world_prompt()
    else:
        battle_dict[location]()

open_dict = {"a3": a3, "b4": b4, "c1": c1}

def open_it(location):
    while worldmap[location][SOLVED]:
        print("You've already ransacked the place.")
        world_prompt()
    if location in ["a3","b4","c1"]:
        open_dict[location]()
    else:
        print(worldmap[location][OPEN])
        world_prompt()

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
OPEN = "opened"
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
                   ZONENAME: "Boss's office",
                   DESCRIPTION: 'description',
                   OPEN: "opened",
                   SOLVED: False,
                   UP: "",
                   DOWN: "a2",
                   LEFT: "",
                   RIGHT: "b1",
                  },
            "a2": {
                   ZONENAME: "",
                   DESCRIPTION: "description",
                   OPEN: "opened",
                   SOLVED: False,
                   UP: "a1",
                   DOWN: "a3",
                   LEFT: "",
                   RIGHT: "b2",
                  },
            "a3": {
                    ZONENAME: "Kitchen",
                    DESCRIPTION: "",
                    OPEN: "Nothing here.",
                    SOLVED: False,
                    UP: "a2",
                    DOWN: "a4",
                    LEFT: "",
                    RIGHT: "b3",
                   },
            "a4": {
                    ZONENAME: "",
                    DESCRIPTION: 'description',
                    OPEN: "opened",
                    SOLVED: False,
                    UP: "a3",
                    DOWN: "",
                    LEFT: "",
                    RIGHT: "b4",
                   },
            "b1": {
                   ZONENAME: "Receptionist's office",
                   DESCRIPTION: 'description',
                   OPEN: "opened",
                   SOLVED: False,
                   UP: "",
                   DOWN: "b2",
                   LEFT: "a1",
                   RIGHT: "c1",
                  },
            "b2": {
                   ZONENAME: "Sales lead's office",
                   DESCRIPTION: "It's an office, baby.",
                   OPEN: "opened",
                   SOLVED: False,
                   UP: "b1",
                   DOWN: "b3",
                   LEFT: "a2",
                   RIGHT: "c2",
                  },
            "b3": {
                    ZONENAME: "Financial Analyst's office",
                    DESCRIPTION: 'description',
                    OPEN: "opened",
                    SOLVED: False,
                    UP: "b2",
                    DOWN: "b4",
                    LEFT: "a3",
                    RIGHT: "c3",
                   },
            "b4": {
                    ZONENAME: "Printer room",
                    DESCRIPTION: 'description',
                    OPEN: "opened",
                    SOLVED: False,
                    UP: "b3",
                    DOWN: "",
                    LEFT: "a4",
                    RIGHT: "c4",
                   },
            "c1": {
                   ZONENAME: "Conference Room",
                   DESCRIPTION: 'description',
                   OPEN: "opened",
                   SOLVED: False,
                   UP: "",
                   DOWN: "c2",
                   LEFT: "b1",
                   RIGHT: "",
                  },
            "c2": {
                   ZONENAME: "Your 'office'",
                   DESCRIPTION: "Your 'office' is in a converted storage closet.\n"
                                  "Your mouse and keyboard are there, but they've neglected to give you a monitor.",
                   OPEN: "You have no monitor, so there's nothing for you to do.",
                   SOLVED: False,
                   UP: "c1",
                   DOWN: "c3",
                   LEFT: "b2",
                   RIGHT: "",
                  },
            "c3": {
                    ZONENAME: "Data Analyst's office.",
                    DESCRIPTION: 'description',
                    OPEN: "opened",
                    SOLVED: False,
                    UP: "c2",
                    DOWN: "c4",
                    LEFT: "b3",
                    RIGHT: "",
                   },
            "c4": {
                    ZONENAME: "IT Room",
                    DESCRIPTION: "The room is crowded with boxes of cables, broken servers and "
                                   "\na sullen looking man staring at his computer screen.",
                    OPEN: "You open one of the drawers and peek inside. More cables.",
                    SOLVED: False,
                    UP: "c3",
                    DOWN: "",
                    LEFT: "b4",
                    RIGHT: "",
                   }

}  






title_screen()
    
    
    
    
          
          
          
          
        