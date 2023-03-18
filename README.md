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

# Flowcharts and discussion of game-logic

To be added

# Technologies used

Python
Gitpod and GitHub Desktop as IDE

# Deployment

All code entered into its respective file from within gitpod.

The source is hosted at github and deployed using the publicly availabe git-hube page of https://github.com/jonthorell/PirateIsland

## Deployment to GitHub Pages

NOTE: The game can of course not run from there. It is used as storage-area for files needed by this readme.

The site was deployed to GitHub pages. The steps to deploy are as follows:

- In the GitHub repository, navigate to the Settings tab
- From the menu on left select 'Pages'
- From the source section drop-down menu, select the Branch: main
- Click 'Save'
- A live link will be displayed in a green banner when published successfully.

Changes in the code is regularily pushed into the repository using:

* git add .
* git commit -m "commit message"
* git push

## Deployment to Heroku

TO-BE-ADDED

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

More to be added

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





Add results and comments

# To-do

1. Re-factor the code in create.py so it is easier to read
2. Change all output so it will fit in 80-columns.
3. Re-do the instructions into several pages

# Credits

All code is by me. Syntax and examples have been looked at on [w3schools](https://www.w3schools.com/python/) but no code is lifted right
out of there.