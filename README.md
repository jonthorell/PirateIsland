# PirateIsland

The aim of this project is to create a working game in the interactive-fiction style in the style of games from say Infocom, but nowhere
near the complexity of their classic games.

![mockup-picture](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/mockup.PNG?raw=true)

# Background

For those unfamiliar with the game-style, it is bascially a game where the player walks around in a fictional setting solving puzzles
using only keyboard commands such as "go east", "inventory", "open door", "examine hat" etc. The aim is to, of course, set solve the
game. 

The games are usually somewhat open-ended in that there are several paths one might take to solve it and one does not necessarily have
to do things in a certain order.

The games also often contain objects and locations that can only be considered red herrings to throw the player off but won't be necessary
to actually finish the game.

If some of the descriptions and names sound familiar it is probably because they are...the map as well as some names are shamelessly stolen
from the game "The secret of Monkey Island" (a graphical adventure game). Some descriptions of objects have been lifted out of "The lord of
the rings". And the name of a character encountered comes from "Red Dwarf".

Three screenshots to give a better idea of how it might look like:

![island1](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/island1.PNG?raw=true)
![island2](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/island2.PNG?raw=true)
![island3](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/island3.PNG?raw=true)

The game is live here:

https://pirate-island.herokuapp.com/

# Scope

The game can be solved, but is deliberately limited in size. Both when it comes to the number of "rooms" the player can visit and
the number of words available to the player.

However, the "engine" behind the game became quite flexible in the end can be expanded as much as one wants.

This particular game should be considered more or less a proof-of-concept of how one can write this kind of game in a flexible manner.

# Background on how the map works

The map is essentially a grid. For this game, it is a 4 rows and 4 columns but that can be changed easily to say 10x10 if that is what your game requires. And not all positions need
to be used.

This is the map used for PirateIsland

![map](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/map.PNG?raw=true)

And here is a link to a text-file with a walk-through. There are more things that can be done
in the game, but that is all that is necessary.

https://github.com/jonthorell/PirateIsland/blob/main/readme-files/walkthrough.txt

# Design considerations (visual)

The output is of course text-only. Some different colors are used though.

In the game proper they are:

Default console-color for the main part.
* Red is used when the game encounters a problem such as when it does not understand a verb.
* Green is used to print out the directions one can travel in as well as things that can be seen
* Yellow is used to print what the player is carrying as well as the help-text

# Design considerations (code)

The game consists of 4 python files:

* run.py, starts the game and initializes everything. The main game loop is also here
* create.py, creates the lists and dicts the game uses to keep track of things
* welcome.py, shows initial help and background at game start
* functions.py, the file where all the game logic takes place

* The project uses two global variables. Maybe not ideal but I settled for that due to:
  * They are used in many functions (and some functions called by other functions) so it made sense to me to have them as globals
  * For the most part the functions only need to read the value of the global variable, so the risk of variable-value conflict is small
  * The project does not rely on external libraries and/or frameworks so external "things" will not introduce a variable of the same name
  
## Flowcharts and discussion of game-logic

The flowchart for run.py looks like this:

![flowchart-run.py](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/flowchart_run.png?raw=true)

As can be seen from the flowchart, control is passed to functions.py in three places.

First when it is imported from run.py. This essentially "creates" the functions and initial values of some variables.

Secondly, to split the input into one verb and possibly a noun as well.

The flowchart for that function looks like this:

![flowchart-parser](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/flowchart_parser.png?raw=true)

Finally, to check the input. It validates what the user typed and what to do with that information.

The flowchart for that is as follows:

![flowchart-check-input](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/flowchart_check_input.png?raw=true)

## Functions

* run.py has no functions. It only calls functions in the other files.
* welcome.py has three functions.
    - welcome(), prints a welcome message
    - hint(), prints a hint about the verbs command
    - print_intro(), sets the background story of the game
* create.py has four functions
    - createObjects(), creates all objects the user can interact with
    - createNouns(), creates all the nouns the game understands
    - createVerbs(), creates all the verbs the game understands
    - createLocations(), creates all the locations the player can visit
* functions.py has 35 verbs. One for each verb the game understands as well as some helper-functions. The complete list is (without parameters):
    - 	print_green(), prints text in green
    -	print_header(), prints text in header color
	-	print_blue(), prints text in blue
	-	print_red(), prints text in red
	-	print_cyan(), prints text in cyan
	-	print_yellow(), prints text in yellow
	-	parser(), splits input into verb and noun
	-	check_input(), checks if input is valid and redirects to correct verb-function.
	-	print_verbs(), prints a list of available verbs
	-	print_location(), prints the current location
	-	print_direction(), prints which ways the player can move
	-	set_verbose(), turn on verbose mode
	-	set_brief(), turn off verbose mode
	-	inventory(), print what the player is carrying
	-	you_can_see(), prints what is available at the current location
	-	go_west(), go west
	-	go_east(), go east
	-	go_south(), go south
	-	go_north(), go down
	-	go_up(), go up
	-	go_down(), go down
	-	hint(), shows a small hint at some locations
	-	wear(), lets the player wear some items
	-	remove(), lets the player "unwear" some items
	-	dead(), used when the player dies. Ends the game
	-	read(), lets the player read some items
	-	v_break(), lets the player break some things
	-	get_noun_by_id(), returns id of noun player entered. Used in if/elif/else clauses
	-	get(), lets the player pick up certain things
	-	drop(), lets the player drop some things
	-	v_open(), lets the player open some things
	-	use(), lets the player use some things
	-	examine(), lets the player examine some things
	-	print_instructions(), prints the "manual"
	-	requires_noun(), used from verb-functions where the player must enter a noun
	
The general flowcharts above should be sufficient to understand the basic logic of how the code works.

However, one additional is necessary. That is for the verbs that require a noun. The verbs that do not
require a noun only ignores everything after the first space character, which means that a nonsense 
sentence like "north is the new orange" is treated as if the player just typed north.

The function for a verb that requires a noun takes the noun as a parameter, like so:

```python

def read(noun):

```
At the start of every multi-word-function the following code is executed:

```python
	
	# code block 1
	result = get_noun_by_id(noun)
    match = result[0]
	# gets the id of the noun entered by comparing what was entered
	# with the combined noun list/dict
	# Returns zero if the noun is not found in the list
    error = requires_noun(noun)
	# Function requires_noun() prints "This verb requires a noun" if none was entered and returns True
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        error = "I don't know how to examine that, mate."
        error += 'What is a "' + noun + '"?'
        print_red(error)
		# no match, so print a message that the game has no idea of what to do and return to prompt
        return
    else:
        noun_id = result[1]
		# the id of the noun is returned as the second item of a tuple, so that can be used in an if-statement

```

See the comments in the code for how it works.

Flowchart for a generic multi-word funcion looks like this:

![flowchart-verb-noun](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/verb_noun_function.png?raw=true)

The verb-specific logic also needs to be adressed. It is quite similar for every verb. The code itself is not hard to follow
or understand. It is basically only a bunch of if/elif/else statements per function.

What is necessary to understand is how to build those statements. It is not hard, but we first need to discuss the data-structures.

## Data structures

The game uses sets, lists, and dicts to keep track of everything the player do or tries
to do.

The verbs are defined twice. First in a set like this (shortened here):

```python

verbset={"exit","l","help","verbs","look","i","inventory","n","north","s"}

```

That is only to make it possible to check if it is verb the game understands with essentially just one line of code.

It also defined like the following (nouns are also defined that way).


```python

data = {
        "ID": 20,
        "verb": "open"
    }

```

It is the ID number that is used in conditional statements. That way it is easy to add synonyms without having
to deal with even more if-clauses. You only need an addional dict like above with the same ID but different noun.

Locations are defined like this:

```python

data = {
        "brief": "You are the top of a cliff.",
		# Short description of the location. Shown when
		# player re-visits a place
        "verbose": "Long description",
		# Long description of the location.
		# Shown on first visit or when player uses the verb look
        "outdoors": True,
		# Is the location outdoors?
		# It never got used in this game but the intention at first
		# was to have some random events happening only when the
		# player is outdoors.
		# Left it in place in case I want to add it later on
        "visited": False,
		# Has the player visited the place before? Used to
		# determine if brief or verbose should be printed
        "east": 0,
		# Value 0: player can not go that way
		# Value >0: if going east, move to that
		# location
        "west": 0,
        "south": 6,
        "north": 0,
        "down": 0,
        "up": 0
    }

```

And objects like this:

```python

data = {
        "ID": 2,
		# id: used in if/elif statements
        "noun": "bottle",
		# the noun in cleartext.
        "description": "a dirty old bottle",
		# what is printed in "You can see:" or
		# in inventory
        "exam": exam,
		# The text printed when player examines the
		# object. In this case, the value of
		# variable exam
        "location": 4,
		# in which location is the object
		# -1 = being carried
        "gettable": True,
		# can it be picked up?
        "visible": True
		# is it visible?
		# used in two ways:
		# 1 a object can be invisible until the player has done
		# something else first. 
		# 2 The object is immovable and described in the verbose text
		# of the location. It is still an object though than can be
		# examined. In order for it to not show up in "You can see:"
		# as well, it needs to be invisible
    }

```

The dicts are nested within lists. The verb-dict is nested within a verb-list and so on. That way they can be treated
like a multidimensional array.

For example, to change whether it is possible to go east from location the player is currently at, one only needs to
do like this:

```python

locations[current_location]['east'] = 17

```

Quite straight-forward and very flexible. Descriptions of the objects can be updated in a similar manner:

```python

objects[2]['exam'] = "The bottle is broken."

```

Updates the exam-text of object 2 if it gets broken somehow.

Theoretically the same could be done with the nouns and verbs, but in this example game it is not utilized.

## if/elif/else per function

So with all that in mind, how does one build the logic in how the verbs work?

The "problem" lies in figuring out which variables and/or list/dicts needs to be compared for the logic to make sense.

An example to illustrate.

Open chest

Naturally, this takes place in the v_open(noun) function.

```python

if current_location == 7 and noun_id == 1:
        if objects[20]["visible"] is False:
            pr_str = "With great effort, you open the chest."
            pr_str += "Inside it you find a small key."
            print(pr_str)
            objects[20]["visible"] = True
        else:
            print("But the chest is already open.")
elif current_location == 8 and noun_id == 19:
		print("You can not open the gate.")
else:
		print("I'm sorry, I don't know how to open that.")
```

That code is added just below the code earlier marked with code block 1.

The chest can not be moved so it is always at location 7, as defined in the object.
The noun entered was chest, which is noun_id 1. Noun_id and the object must have
the same ID for this logic to work. There is an excel-file within the readme-files
folder that I used to keep track of it. As mentioned elsewhere, if you have two
nouns defined with the same ID they are treated as synonyms.

So, line 1 of this code-block checks whether the player is at location 7 (see map)
and used noun_id 7, which corresponds to the chest.

The nested if-clause checks if the chest has been opened already or not. That can no
doubt be accomplished in other ways as well. In this case, the easiest way of checking
it was to see if the key (object id 20) had been made visible or not. When it is false,
the chest is unopened. As soon as the chest has been opened, the key is made visible
and thus the else-statement is triggered if one tries to open the chest again.

The elif-statement checks for the next combination of location and noun where the player
might try opening something. If the developer thinks of something else the player might
try to open, just add another elif into the mix.

Finally, an else to make sure the player always gets some feedback even if it is just
to let them know they onto the wrong track.

Every verb-function work in the same way. The only difference is in what to check for
in the if-clauses.

# Requirements

The game has no external dependencies in form of libraries and frameworks.
The only requirement is that python itself is at least version 3.10.

The requirements.txt file does not necessarily reflect that. The dependencies listed there are
installed in my local environment, but not used in this project.

As far as deployment to heroku is concerned, it does not hurt to have them there.
See further under deployment.

# Technologies used

* Python
* Gitpod
* GitHub Desktop as IDE
* Heroku

# Deployment

All code entered into its respective file from within gitpod. At first deployment. After that, everything was done
using notepad++ and GitHub Desktop. 

The source is hosted at github and deployed using the publicly availabe github page of https://github.com/jonthorell/PirateIsland

## Deployment to Heroku

In order to deploy something to Heroku, several steps needs to be taken care of.

This is taken for granted that the project is already hosted at GitHub.

Code changes are regularily pushed into that repository using either Github Desktop or the cli command git using:

* git add .
* git commit -m "commit message"
* git push

The steps for deployment to Heroku are:

1. Create an account at Heroku.
2. Create an app in Heroku, with a unique name and a region
3. Under settings, create an environment variable with the name PORT and value of 8000
4. This project does not need it, but if it did: create a variable with the name creds and the credential needed to access external resources.
5. In gitpod (or locally if you prefer to work that way), do: pip freeze > requirements.txt to add the requirements needed to build the project at heroku.
6. Things installed, if any, locally will be added to the requirements file, to make sure everything necessary will be available when deployed.
7. This might include things not necessarily referenced, but it will make sure the build will be complete.
8. Create the buildpacks. For this project, python and nodejs (in that order)
9. Under deployment, connect the github account to the heroku-account
10. Under deployment method, connect the app to the correct github repository
11. Decide if you want the deployment to be automatic or manual. That is a matter of preference. For now, I have opted to make it manual.

# Testing

Most functions can be tested in isolation. That is, the functions that corresponds to a specific verb.

The helper-functions can not though. Especially not parser(), check_input(), get_noun_by_id(), and requires_noun()

parser() and check_input() were the two first functions written. They were actually written outside of project scope at first
to get the hang on string-handling. And without being in a function at the time.

As such, a lot of print-statements were used to make sure the variables got the values I expected. 

* parser()

    1. Checked value of string2 after all occurenes of " the " had been removed (and other determiners)
    2. Checked he contents of the variable verb after the first split.
    3. Checked the "reminder" after the first split
    4. Checked if no_of_words is what it should be (either 1 or 2)
    5. Checked the values of i and noun at every iteration of the loop
    6. When converted to a function, check that the returned tuple contains the verb in [0]
    7. And the noun in [1]. Except if only word was entered, then [1] should contain "None"

    After testing with input strings of different lengths when it comes to the number of words I am confident that the
    returned tuple will always be a one-word verb in [0] and a one-word noun in [1]

* check_input()

    1. Print the value of array_id and verb at every step in the loop
    2. Compare with the excel sheet if the values match. That is, if the verb is north the array_id should be 5.
    3. In the match/case statements, print some easily recognized text in the function called. Like so:

    ```python
    case 6:  # go south
                go_south()
    ```

    ```python

    def go_south():
    	print("Go south function")

    ```

    Do that for every verb. When you get the correct output for every verb, you know the check_input() function
    works as intended and you can add functionality to the verb-functions.

* get_noun_by_id()

	```python
    def get_noun_by_id(noun):
    """
    Function get_noun_by_id() finds the id of the noun the player
    typed and returned back to the calling function, where it is
    used in if-else caulses to see if what the player tried to do
    makes sense
    """
    match = 0  # initial value. If still 0 at end of loop, no match
    for i in range(len(nouns)):
        curr_noun = nouns[i]
        array_noun = curr_noun["noun"]
        array_id = curr_noun["ID"]
        if array_noun == noun:
            match = 1
            print(array_noun,noun,array_id,array_noun == noun,match)
            return match, array_id
    print(array_noun,noun,array_id,array_noun == noun,match)
    return match, array_id
	```
	
	If the get_noun_by_id() is temporarily changed like this, one can see what is returned.
	
	The output when a correct noun is input should be like this (assuming the noun is ship in this example):
	
    * ship ship 15 True 1
	
	On the other hand, if an unknown noun is entered you will get this:
	
	* sand gandalf 23 False 0
	
	1. sand is the last noun defined.
	2. gandalf is what was actually entered in the input
	3. 23 is the ID of the last defined noun (sand)
	4. The value is False since "sand" and "gandalf" does not match
	5. Consequently, the return value is 0.
	
	When those values are checked from the calling function (say v_open), what happens is:
	
	1. If match == 0, the noun is not recognized. "What is a _insert_noun_" is printed to the console, and returns to the prompt. In this case, the noun_id is irrelevant since it will never be checked.
	2. Otherwise, return the id to be used in if/else statements.
	
	The most important thing to check here is regarding synonyms.
	
	"examine house" and "examine building" should both return noun_id 12 (which it does).

* requires_noun()

    This one is easy to check. The code with the comment "code block 1" should be included in every funcion that requires a noun. If it has been left out in say examine(),
	the player would not get "But this verb requires a noun!" if they try examine on its own.
	
The verb-specific verb-functions() can and was tested more-or-less in isolation. That is, the different conditions for a verb can be tested one by one.
To continue with the example of "Open chest". There are two conditions apart from using the correct noun.

1. The player is at the	correct location.
2. Whether or not it has been opened already.

So, what is needed is to test:

1. What happens if one tries to open it at some other location?
2. Is the object updated as it should so the chest can be opened only once?

The chest is relatively straight-forward. But the key in it is needed to unlock a door.

In that case, it needs to be checked:

1. Do the player have the key?
2. Is the player at the correct location?
3. Has the door been unlocked already?
4. Has the door been opened already?

Same thing here regarding which objects are being manipulated to indicate if the player has successfully done each step along
the way.  

Repeat for every verb and every condition. In the case of opening the door, two verbs are involved so both functions obviously needs
to be checked. And both verbs have other conditions as well that may trigger something else. 

Therefore, it is probably a good idea to have a notebook ready to write down things that does not do what is to be expected and look
further into the code and see where the problem could be.

One very likely suspect is when you check for values for an object that can not be refered to by noun_id.

Like this:

```python
if objects[6]["visible"] is False:
objects[6]["visible"] = True
```

Make sure the [6] is refering to the correct item. Both in the if-statement and the assign-statement. And especially that it
is the same object!

It is timeconsuming but since the code needed for the conditions is pretty similar everywhere some bugs can sometimes be spotted
by just looking at the code without actually testing. It should, of course, be tested anyway.

In order to speed up testing, it is easy enough to alter the initial values. That is, to make sure the player starts at the
correct location and already with the key in his/her possession.

And finally, play through it from start to finish so one is sure that the game actually can be finished. 

# Bugs encountered and fixed

1. The commands verbosity and brief did not toggle the flag correctly. The problem was that those two commands alter a global variable and I forgot the global keyword.

2. Sometimes the drop verb did not seem to drop the object. It was removed from the inventory but did not turn up at the new location. Turns out this was a debugging problem.
When testing a new function with dependencies (use key in location 15 for example) I forcibly set they key-object to be a part of the inventory. Just to easily check all
conditions. When dropping the key it was removed from the inventory but did not show up at the location. Turned out it was an oversight in my thinking when checking and not
the code. The key needs to be found before it can be used so it has the key-value "visible": False set. If one plays the game as the user will see it (or indeed, setting it
to true at start) the logic works as expected.

3. Many strings were too long to display properly without overflow. Fixed by adding \n at strategic places to hardcode the length for a terminal 80 columns wide.

4. When examining the skeleton twice, the second time a blank string was printed. Was a mistake when fixing the overflow problem so the variable was accidentally set to null.

5. Examining the skeleton did not use the correct key:value value. It used a hard-coded string. A left-over from some debugging.

6. A similar problem as 5 was discovered for examining the ring. Both fixed.

7. Many smaller mistakes that created syntax-errors, such as missing the : after the def-statement, accidentally typed = instead of == and stuff of that nature. Fixed on the spot.

8. Missed a check in the functions where a noun is required. The check was whether or not the player had actually typed in two words. Fixed by adding a new function that is called from
the affected verb-functions.

9. Some output (read: a lot) did not take the 80-column width into enough consideration. Most, if not all, of those should be fixed by now. If it has been missed somewhere it may look odd whenever
that is printed to the console, but it does not affect functionality in any way.

10. One bug showed up when deployed to Heroku. An oversight really, since I had some special code in place to get ansi-colors to work in the standard cmd.exe console in windows. Which, of course, is not
needed on a linux-machine so an error popped up. The game was still playable though, but it did not look good with that error. Removed the offending code since it was not necessary anymore.

# Remaining bugs

None known.

# Validation

All code run through: [ci-linter](https://pep8ci.herokuapp.com/)

* run.py checked. Some whitespace issues corrected. When correcting those issues, made sure output is limited to 80 columns as well.

![linter-run.py](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/run_py_check.PNG?raw=true)

* welcome.py checked. Some whitespace issues corrected and made sure output stays within the limits of 80 columns as well

![linter-welcome.py](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/welcome_py_check.PNG?raw=true)

* create.py checked. Some whitespace issues here as well, plus quite a few lines that were too long. Made sure output for all
objects stays within the 80 column limitation as well.

![linter-create.py](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/create_py_check.PNG?raw=true)

* functions.py fully compliant. This one was run through "black" for an automated process. Or maybe I should say semi-automatic.
There were some issues left that I fixed manually, mostly due to line-lengths.

![linter-functions.py](https://github.com/jonthorell/PirateIsland/blob/main/readme-files/functions_py_check.PNG?raw=true)

The original functions.py is stored in readme-files in case it is not okay to use the "black" tool.

# To-do

1. Change all output so it will fit in 80-columns.


# Credits

All code is by me. Syntax and examples have been looked at on [w3schools](https://www.w3schools.com/python/) but no code is lifted right
out of there.

Black helped out with making sure the code is PEP8 compliant.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)