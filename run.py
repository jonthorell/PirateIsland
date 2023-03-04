# Git commit messages are not as encompassing as they 
# should be. That is because I did a lot of work 
# locally using just notepad++ and python installed.
# while experimening and figuring out what my project should be

# import my own functions. 

# Divided in three for readability and manageability
# Makes it easier to concentrate on the code in question

# welcome-functions. Only used at game-start, and data that is unchanged during the game
# create. Creates the different objects etc the player can interact with. Some will be altered during game.
# functions. The main game-logic is in this import.

import functions            #main functions
import welcome              #functions for initial greetings, help-texts
import create               #functions for creating objects, nouns, locations & verbs

#welcome.welcome()
functions.print_instructions()
#welcome.hint()
#welcome.print_intro()
create.createVerbs(functions.verbs)
create.createObjects(functions.objects)
create.createNouns(functions.nouns)
create.create_locations (functions.locations)

#raise SystemExit('Placeholder to not starting the game for checking variables')

# name=input("What is your name? ")



name="Jonas"

turns=0
functions.print_location(functions.current_location,1)
game_in_progress=True

while game_in_progress:
    user_input=input(f"\n{name}, what is thy bidding? ")
    user_string=functions.parser(user_input)
    if user_string is not None:
        verb=user_string[0]
        noun=user_string[1]    
        value=functions.check_input(verb,noun,name)
        if value==50:
            print("---------------------")
            print("Thank you for playing.")
            print("Your game took "+str(turns)+" turns.")
            game_in_progress=False
        else:
            turns+=1