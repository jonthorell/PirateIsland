# Git commit messages are not as encompassing as they 
# should be. That is because I did a lot of work 
# locally using just notepad++ and python installed.
# while experimening and figuring out what my project should be
# But still quite a lot of commits

# import my own functions. 

# Divided in three for readability and manageability
# Makes it easier to concentrate on the code in question

# welcome-functions. Only used at game-start, and data that is unchanged during the game
# create. Creates the different objects etc the player can interact with. Some will be altered during game.
# functions. The main game-logic is in this import.

import functions            #main functions
import welcome              #functions for initial greetings, help-texts
import create               #functions for creating objects, nouns, locations & verbs

welcome.welcome()
functions.print_instructions()
welcome.hint()
welcome.print_intro()

# The below creates everything needed for the game-logic
create.createVerbs(functions.verbs)
create.createObjects(functions.objects)
create.createNouns(functions.nouns)
create.create_locations(functions.locations)

while True:
    name=input("What is your name? ")
    
    if name.strip() != '':
        functions.print_red("Welcome "+name+"!\n")
        break
    else:
        functions.print_red("Please provide a name!\n")
#name="Jonas"

turns=0
functions.print_location(functions.current_location,1)
game_in_progress=True

while game_in_progress:
    user_input=input(f"\n{name}, what is thy bidding? ")
    user_string=functions.parser(user_input)    #parser function splits the input string into words and returns it here
    if user_string is not None: #if none, loop back to new prompt
        verb=user_string[0]
        noun=user_string[1]    
        value=functions.check_input(verb,noun,name)     #check for valid inputs, and processing proceeds in functions.py file. Name is passed to be able to customize some string with username
        if value==50:       #if the input is quit, return 50 to terminate the game
            print("---------------------")
            print("Thank you for playing.")
            print("Your game took "+str(turns)+" turns.")
            #print("\n")
            #print(create.createObjects.__doc__)
            game_in_progress=False      #break out of while-loop
        else:
            turns+=1    #increase the number of turns that has been used