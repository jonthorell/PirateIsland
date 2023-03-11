![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome jonthorell,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

## Bugs encountered

the commands verbosity and brief did not toggle the flag correctly. The problem was that those two commands alter a global variable and I forgot the global keyword.

sometimes the drop verb did not seem to drop the object. It was removed from the inventory but did not turn up at the new location. Turns out this was a debugging problem.
When testing a new function with dependencies (use key in location 15 for example) I forcibly set they key-object to be a part of the inventory. Just to easily check all
conditions. When dropping the key it was removed from the inventory but did not show up at the location. Turned out it was an oversight in my thinking when checking and not
the code. The key needs to be found before it can be used so it has the key-value "visible": False set. If one plays the game as the user will see it (or indeed, setting it
to true at start) the logic works as expected. Silly me.

## Comments

The "engine" behind this example-game is really flexible. The scope of this particular game is quite limited, but the idea of how it works can be expanded as much as one wants.
The map is essentially a grid. For this game, it is a 4 rows and 4 columns but that can be changed easily to say 10x10 if that is what your game requires. And not all positions need
to be used.