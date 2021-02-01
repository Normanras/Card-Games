#Scavenger Hunt Game Error Verification

# Python RPG 

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### Player Setup #####
class player:
    def __init__(self):
        self.name=''
        self.hp=0
        self.mp=0
        self.status_effects=[]
        self.location = 'start'
myPlayer = player()

#### Title Screen Setup ####
def title_screen_selections():
    option = input("> ")
    if option.lower == ("play"):
        start_game() #placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() #placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('##########################')
    print('#                        #')
    print('#                        #')
    print('#   WELCOME TO THE GAME  #')
    print('#                        #')
    print('#                        #')
    print('##########################')
    print('        === PLAY ===      ')
    print('        === HELP ===      ')
    print('        === QUIT ===      ')
    print('==========================')

def help_menu():
    pass 
#placeholder to put help menu items 

##### GAME FUNCTUATLITY ####
def start_game():



##### MAP ####

#| a7  | a8  | a9  | 
#-------------------
#| a4  |  a5 | a6  |
#-------------------
#| a1  | a2  | a3  |

    DESCRIPTION = 'description'
    EXAMINATION = 'examine'
    SOLVED = False
    UP = 'up','north'
    DOWN = 'down','south'
    LEFT = 'left','west'
    RIGHT = 'right','east'

solved_places = {'a1':False, 'a2':False, 'a3':False, 'a4':False,
                 'a5':False, 'a6':False, 'a7':False, 'a8':False, 'a9':False}

zonemap = {
    'a1':{
        ZONENAME: "Kitchen",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'a4'
        DOWN = ''
        LEFT = ''
        RIGHT = 'a2'
    },
    'a2':{ 
        ZONENAME: "Foyer/Entry",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'a5'
        DOWN = 
        LEFT = 'a1'
        RIGHT = 'a3'
    },
    'a3':{
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'a6'
        DOWN = 
        LEFT = 'a2'
        RIGHT = ''
    },
    'a4':{
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'a7'
        DOWN = 'a1'
        LEFT = ''
        RIGHT = 'a5'
    },
    'a5':{
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'a8'
        DOWN = 'a2'
        LEFT = 'a4'
        RIGHT = 'a6'
    },
    'a6':{
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = 'a9'
        DOWN = 'a3'
        LEFT = 'a5'
        RIGHT = ''
    },
    'a7':{
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = ''
        DOWN = 'a4'
        LEFT = ''
        RIGHT = 'a8'
    },
    'a8':{
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = ''
        DOWN = 'a5''
        LEFT = 'a7'
        RIGHT = 'a9'
    },
    'a9':{
        ZONENAME: "",
        DESCRIPTION = 'description'
        EXAMINATION = 'examine'
        SOLVED = False
        UP = ''
        DOWN = 'a6'
        LEFT = 'a8'
        RIGHT = '' #Perhaps a secret door that moves you to a5?
    }
}