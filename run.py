# Git commit messages are not as encompassing as they 
# should be. That is because I did a lot of work 
# locally using just notepad++ and python installed.
# while experimening and figuring out what my project should be

# import my own functions. They are in a separate file to make the code easier to read
# and game-file itself only contain the main loop and the initialization code
# This of course requires that a lot of the functions require parameters and 
# return-values
# Which is good-practice anyway

import functions

# functions.welcome()
functions.print_intro()
functions.createVerbs()

# name=input("What is your name? ")

functions.create_locations ()

name="Jonas"

turns=0
functions.print_location(functions.current_location,1)
game_in_progress=True

while game_in_progress:
    user_input=input(f"{name}, what is thy bidding? ")
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