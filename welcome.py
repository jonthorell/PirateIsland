from functions import print_header,print_green,print_cyan,print_yellow

def welcome():
    print_header('Welcome to "Pirate Island"')
    print ("A miniature interactive-fiction game")
    print ("An example of how such a game can be written in python")
    print ("The game is not very big, and for experienced players of the genre most likely solved very quickly.")
    print ("But as a long-time fan of the genre, great fun to play with it again!")
    print ("------------------------")
    print_instructions()
    
    hint="\nHint: The earliest games of this type had a tendency to have 'guess-the-verb-to-be-used' puzzles included. Not by design for the most part, but whether by design or limitations "
    hint+="of the hardware at the time it is annoying, and something I do not like myself. For that reason I added the command 'verbs' to display all the verbs the game understands."
    print_green(hint)
    input("Press Enter to start...")
    

def print_intro():
    intro='You, as one of the crewmembers of the notorious pirate wessel "The Sea Monkey" is (or should I say was) on a journey for glory, fame and riches galore.'
    intro+=" \nYour captain, a certain Captain LeChuck, is as bloodthirsty and notorious as the ship."
    intro+="\n\nNeeedless to say, Governer Marley is not too keen on what you are doing so he sent another ship to take you down. That ship was piloted by a Jack Sparrow, the scourge"
    intro+=" of pirates everywhere."
    intro+=" \nThe ship attacked you just outside this isolated island, name unknown.\nTo you and your fellow pirates misfortune they were far better trained and even worse: far better equipped."
    intro+="\n\nYou didn't have a chance. They defeated you very thoroughly and humilatingly quickly."
    intro+='"The Sea Monkey" is sinking rapidly and most of your crew-mates are dead. Including Captain LeChuck.' 
    intro+="\n\nYour only chance is to swim ashore and then somehow find your way back to civilazation."
    print_cyan(intro)
    input("Press Enter to continue...")
    
def print_instructions ():
    rules="\nInteractive fiction is purely text-based, and can be considered a story where the player takes charge of the outcome rather than just reading along. The player moves around in the game by issuing commands. These commands consists of one or two words, in a verb-noun pattern."
    rules+="Some verbs work on their own (inventory for example), others need a noun (open door for example). The idea is that you walk around in a fictional world and solves puzzles along the way. A puzzle can be"
    rules+=" (for example) finding the key to a locked door so it can be unlocked and the player can get further into the world displayed. A typical game is usually littered with information and objects that the player"
    rules+=" thinks might be important, but in the end serves only as distractions."
    rules+='\n\nEverything after a second word will be discarded. If you enter a command such as "inventory list" and the verb (inventory) does not expect a noun, the noun will be discared as well.'
    rules+="\n\nDirections are always entered with just the direction. That is, it is a one-word sentence. Either 'north' or 'n' will suffice. Go north is unneccesary."
    rules+="\n\nIn other words: everyting you need to do can be accomplished by either a one or a two-word command. Nothing fancier than that is ever required."
    rules+="\n\nIf you need to, you can view these instructions again with the command help."
    print_yellow(rules)