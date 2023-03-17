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