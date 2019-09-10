## Intern: The Game

import random
import cmd
import textwrap
import sys
import os

screen_width = 100

#### Player Setup ####

class Player():
    
    def __init__(self,name):
        self.name = name
        self.will = 100
        
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
    print('-Placeholder text.')
    title_screen_selection()
    

    
          
          
          
          
          
        