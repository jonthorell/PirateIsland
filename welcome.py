# This file is only used at game-start to print introdoctory
# text and instructions

from functions import print_header, print_green, print_cyan, print_yellow


def welcome():
    """
    Function welcome() used at game start to provide a mini intro
    to the game-genre
    """
    print_header('Welcome to "Pirate Island"')
    print("A miniature interactive-fiction game.")
    print("An example of how such a game can be written in python.")
    print("The game is not very big, and for experienced players")
    print("of the genre most likely solved very quickly.")
    print("But as a long-time fan of the genre, great fun to", end=" ")
    print("play with it again!")
    print("------------------------")
    input("Press Enter to continue...")


def hint():
    """
    Function hint() just used to provide info abouth the command verbs
    """
    hint = "\nHint:\nEarly games of this type had a tendency"
    hint += " to have 'guess-the-verb-to-be-used'\npuzzles included."
    hint += "Not by design for the most part, but whether by design"
    hint += " or\nlimitations of the hardware at the time is is"
    hint += " annoying, and something I do\nnot like myself. For"
    hint += " that reason I added the command 'verbs' to display"
    hint += "\nall the verbs the game understands."
    print_green(hint)
    input("Press Enter to start...")


def print_intro():
    """
    Function print_intro() just prins the background story of the gamne
    """
    intro = "You, as one of the crewmembers of the notorious pirate wessel"
    intro += "\"The Sea Monkey\"\nis (or should I say was) "
    intro += "on a journey for glory, fame and riches galore."
    intro += " \nYour captain, a certain LeChuck, is as bloodthirsty and "
    intro += "notorious as the ship."
    intro += "\n\nNeeedless to say, Governer Marley is not too keen on "
    intro += "what you are doing so he"
    intro += "\nsent another ship to take you down. That ship was "
    intro += "piloted by a Jack Sparrow, the"
    intro += "scourge of pirates everywhere."
    intro += "\n\nThe ship attacked you just outside this isolated island, "
    intro += "name unknown.\nTo you and your fellow pirates misfortune they "
    intro += "were far better trained and even worse: far better equipped."
    intro += "\n\nYou didn't have a chance. They defeated you very thoroughly "
    intro += "and humilatingly"
    intro += '\nquickly. "The Sea Monkey" is sinking rapidly'
    intro += " and most of your crew-mates are \ndead. "
    intro += "Including Captain LeChuck."
    intro += "\n\nYour only chance is to swim ashore and then somehow find"
    intro += "\nyour way back to civilazation."
    print_cyan(intro)
    input("Press Enter to continue...")
