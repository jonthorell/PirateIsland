def print_instructions ():
    rules="\nInteractive fiction is purely text-based, and can be considered a story where the player takes charge of the outcome rather than just reading along."
    rules+="\nThe player moves around in the game by issuing commands. These commands consists of one or two words, in a verb-noun pattern."
    rules+="\nSome verbs work on their own (inventory for example), others need a noun (open door for example). "
    rules+="\n\nThe idea is that you walk around in a fictional world and solves puzzles along the way. A puzzle can be"
    rules+=" (for example) finding the key to a locked door\nso it can be unlocked and the player can get further into the world displayed. "
    
    rules+="\n\nA typical game is usually littered with information and objects that the player"
    rules+=" thinks might be important, but in the end serves only as distractions."
    rules+='\n\nEverything after a second word will be discarded. If you enter a command such as "inventory list" and the verb (inventory) does not expect a noun, \nthe noun will be discared as well.'
    rules+="\n\nDirections are always entered with just the direction. That is, it is a one-word sentence. Either 'north' or 'n' will suffice. Go north is unneccesary."
    rules+="\n\nIn other words: everyting you need to do can be accomplished by either a one or a two-word command. Nothing fancier than that is ever required."
    rules+="\n\nIf you need to, you can view these instructions again with the command help."
    print_yellow(rules)