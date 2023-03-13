#This file is only used at game-start to print introdoctory text and instructions

from functions import print_header,print_green,print_cyan,print_yellow

def welcome():
    """
    Function welcome() used at game start to provide a mini intro to the game-genre
    """
    print_header('Welcome to "Pirate Island"')
    print ("A miniature interactive-fiction game")
    print ("An example of how such a game can be written in python")
    print ("The game is not very big, and for experienced players of the genre most likely solved very quickly.")
    print ("But as a long-time fan of the genre, great fun to play with it again!")
    print ("------------------------")
    
def hint():    
    """
    Function hint() just used to provide info abouth the command verbs
    """
    hint="\nHint: The earliest games of this type had a tendency to have 'guess-the-verb-to-be-used' puzzles included."
    hint+="\nNot by design for the most part, but whether by design or limitations "
    hint+="of the hardware at the time it is annoying, and something I do not like myself.\nFor that reason I added the command 'verbs' to display all the verbs the game understands."
    print_green(hint)
    input("Press Enter to start...")
    

def print_intro():
    """
    Function print_intro() just prins the background story of the gamne
    """
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
    