## Intern: The Game

import random
import cmd
import textwrap
import sys
import os
import time
from random import uniform

screen_width = 100

#### Player Setup ####

class Player():
    
    def __init__(self):
        # Expects string for name. 
        self.name = name
        self.will = 0
        self.degree = ''
        self.location = 'start'
        self.gameover = False
        # DEGREE?
        
myPlayer = Player()
        
#### Title Screen ####

def title_screen_selection():
    option = input('> ')
    if option.lower() == ('play'):
        start_game()
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print('Please choose an option.')
        option = input('> ')
        if option.lower() == ('play'):
            start_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()
        
def title_screen():
    os.system('clear')
    print('#############################')
    print('##### Intern: The Game ######')
    print('#############################')
    print('           |PLAY|            ')
    print('           |HELP|            ')
    print('           |QUIT|            ')
    title_screen_selection()
    
def help_menu():
    print('Use up, down, left, right to navigate.')
    title_screen_selection()

### GAME INTERACTIVITY ###    

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print('\n' + '====================')
    print('What would you like to do?')
    action = input("> ")
    valid_actions = ['move', 'go', 'walk', 'quit', 'inspect', 'examine', 'interact', 'look']
    while action.lower() not in valid_actions:
        print('Invalid command. Try again friend.')
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'walk']:
        move(action.lower())
    elif action.lower() in ['inspect', 'examine', 'interact', 'look']:
        examine(action.lower())

def move(myAction):
    ask = 'Where would you like to move to?\n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFt]
        movement(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement(destination)

def movement(destination):
    print("\n" + "You have moved " + destination + ".")
    myPlayer.location = destination
    print_location()

def examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print('You have found everything of value')
    else:
        print('Do something here')



    
### GAME FUNCTIONALITY ###

def start_game():
    pass


def main_game():
    while myPlayer.gameover is False:
        prompt()
        # Here handle boss defeated, puzzles solves, etc...

def typewriter(text, start=None, stop=None):
    # Prints out in a typewriter effect.
    # Expects a string
    if start is None:
        start = 0.05
    if stop is None:
        stop = 0.1
    for i in range(len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(uniform(start, stop))

def setup_game():
    os.system('clear')

    # NAME
    question1 = "What's your name, sailor?"
    typewriter(question1)
    myPlayer.name = input("> ")




### MAP ###
### Start in A2.###
"""
   A       B      C
------------------------
|      |       |       | 1
------------------------
|      |       |       | 2
------------------------ 
|      |       |       | 3
------------------------
|      |       |       | 4
------------------------
"""


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False
                 'b1': False, 'b2': False, 'b3': False, 'b4': False
                 'c1': False, 'c2': False, 'c3': False, 'c4': False
                }
    
worldmap = {'a1': {
                   ZONENAME = '',
                   DESCRIPTION = 'description',
                   EXAMINATION = 'examine',
                   SOLVED = False,
                   UP = 'up', 'north',
                   DOWN = 'down', 'south',
                   LEFT = 'left', 'west',
                   RIGHT = 'right', 'east',
                  },
            'a2': {
                   ZONENAME = 'startzone',
                   DESCRIPTION = 'Your desk is in a converted closet.',
                   EXAMINATION = 'examine',
                   SOLVED = False,
                   UP = 'a1',
                   DOWN = 'a3',
                   LEFT = '',
                   RIGHT = 'b2',
                  }
            
}  






title_screen()
    
    
    
    
          
          
          
          
        