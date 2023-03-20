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
* welcome.py, shows initial help and background at game starts
* functions.py, the file where all the game logic takes place

* The project uses two global variables. Maybe not ideal but I settled for that due to:
  * They are used in many functions (and some functions called by other functions) so it made sense to me to have them as globals
  * For the most part the functions only need to read the value of the global variable, so the risk of variable-value conflict is small
  * The project does not rely on external libraries and/or frameworks so external "thing" will not introduce a variable of the same name
  
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
        "verbose": "Long description",
        "outdoors": True,
        "visited": False,
        "east": 0,
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
        "noun": "bottle",
        "description": "a dirty old bottle",
        "exam": exam,
        "location": 4,
        "gettable": True,
        "visible": True
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


## Requirements

The game has no external dependencies in form of libraries and frameworks.
The only requirement is that python itself is at least version 3.10.

The requirements.txt file does not necessarily reflect that. The dependencies listed there are
installed in my local environment, but not used in this project.

As far as deployment to heroku is concerned, it does not hurt to have them there.
See further under deployment.

# Flowcharts and discussion of game-logic

To be added

# Technologies used

Python
Gitpod
GitHub Desktop as IDE

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
5. In your gitpod/github repository, do: pip freeze > requirements.txt to add the requirements needed to build the project at heroku.
6. Things installed locally will be added to the requirements file, to make sure everything necessary will be available.
7. This might include things not necessarily referenced, but it will make sure the build will be complete.
8. Create the buildpacks. For this project, python and nodejs (in that order)
9. Under deployment, connect the github account to the heroku-account
10. Under deployment method, connect the app to the correct github repository
11. Decide if you want the deployment to be automatic or manual. That is a matter of preference. For now, I have opted to make it manual.

# Testing

## Code

TO-BE-ADDED

## Game-play

TO-BE-ADDED

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