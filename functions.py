import os
os.system("")  # enables ansi escape characters in terminal
os.system("cls") #clears the console

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "CYAN": "\033[96m",
    "YELLOW": "\033[93m",
    "ENDC": "\033[0m",
}

verbset={"exit","l","help","verbs","look","i","inventory","n","north","s","south","w","west","e","east","exam","examine","wear","remove","get","take","drop","use","read","dig","climb","verbose","brief","open","close","clear","quit","instructions","exits","directions"}
locations=[]
objects=[]
verbs=[]
current_location=7
verbosity=False
#1=always print verbose text, 0 only at first visit. Altered by verbose and brief functions


def createObjects():
    #the different keys are for:
    #id: internal id to keep track of which object the user interacts with
    #noun: the noun used to refer to it. 
    #description: Displayed in "You can see:" text at location
    #exam: what will be displayed when user examines the object
    #location: initial location. Updated when taken/dropped etc. -1 if being carried
    #gettable: if the object can be taken or not.
    #visible: if the object should be displayed in "You can see:". Used when something must be done before the object reveals itself. 
    #Also used if something is being described in the main-text for objects that are always in a specific location such as a building,
    #boat, etc
    data = {
    "ID": 0,
    "noun": "sword",
    "description": "a cutlass sword",
    "exam": "It is your typical cutlass. Nothing special about it, apart from some stains that appear to be blood.",
    "location": 7,
    "gettable": True,
    "visible": True
}
    objects.append(data)
    
    data = {
    "ID": 1,
    "noun": "chest",
    "description": "a campher wood chest",
    "exam": "The chest looks and smells as if it is made out of campher wood. It looks like it is extremely heavy.",
    "location": 7,
    "gettable": True,
    "visible": False
}
    objects.append(data)
    
    #print(objects)
    #print(len(objects))
    #print(type(objects))
    #current_object_data=objects[0]
    #print(type(current_object_data))
    #print("ID:"+str(current_object_data['ID']))
    #print("noun:"+str(current_object_data['noun']))
    #print("exam:"+str(current_object_data['exam']))
    #print("initial:"+str(current_object_data['initial']))
    #print("gettable:"+str(current_object_data['gettable']))
    #print("visible:"+str(current_object_data['visible']))


def welcome():
    print_header('Welcome to "Pirate Island"')
    print ("A miniature interactive-fiction game")
    print ("An example of how such a game can be written in python")
    print ("The game is not very big, and for experienced players of the genre most likely solved very quickly.")
    print ("But as a long-time fan of the genre, great fun to play with it again!")
    print ("------------------------")
    print_instructions()
    
    hint="\nHint: The earliest games of this type had a tendency to have 'guess-the-verb-to-be-used' puzzles included. Not by design for the most part, but whether by design or limitations "
    hint=hint+"of the hardware at the time it is annoying, and something I do not like myself. For that reason I added the command 'verbs' to display all the verbs the game understands."
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

def print_green(text):
    print(COLOR["GREEN"], text, COLOR["ENDC"])

def print_header(text):
    print(COLOR["HEADER"], text, COLOR["ENDC"])
    
def print_blue(text):
    print(COLOR["BLUE"], text, COLOR["ENDC"])
    
def print_red(text):
    print(COLOR["RED"], text, COLOR["ENDC"])
    
def print_cyan(text):
    print(COLOR["CYAN"], text, COLOR["ENDC"])
    
def print_yellow(text):
    print(COLOR["YELLOW"], text, COLOR["ENDC"])

def print_instructions ():
    rules="\nInteractive fiction is purely text-based, and can be considered a story where the player takes charge of the outcome rather than just reading along. The player moves around in the game by issuing commands. These commands consists of one or two words, in a verb-noun pattern."
    rules=rules+"Some verbs work on their own (inventory for example), others need a noun (open door for example). The idea is that you walk around in a fictional world and solves puzzles along the way. A puzzle can be"
    rules=rules+" (for example) finding the key to a locked door so it can be unlocked and the player can get further into the world displayed. A typical game is usually littered with information and objects that the player"
    rules=rules+" thinks might be important, but in the end serves only as distractions."
    rules=rules+'\n\nEverything after a second word will be discarded. If you enter a command such as "inventory list" and the verb (inventory) does not expect a noun, the noun will be discared as well.'
    rules=rules+"\n\nDirections are always entered with just the direction. That is, it is a one-word sentence. Either 'north' or 'n' will suffice. Go north is unneccesary."
    rules=rules+"\n\nIn other words: everyting you need to do can be accomplished by either a one or a two-word command. Nothing fancier than that is ever required."
    rules=rules+"\n\nIf you need to, you can view these instructions again with the command help."
    print_yellow(rules)

def createVerbs ():
    data = {
    "ID": 0,
    "verb": "exit"
}
    verbs.append(data)
    data = {
    "ID": 1,
    "verb": "help"
}
    verbs.append(data)
    data = {
    "ID": 2,
    "verb": "verbs"
}
    verbs.append(data)
    data = {
    "ID": 3,
    "verb": "look"
}
    verbs.append(data)
    data = {
    "ID": 3,
    "verb": "l"
}
    verbs.append(data)
    data = {
    "ID": 4,
    "verb": "inventory"
}
    verbs.append(data)
    data = {
    "ID": 4,
    "verb": "i"
}
    verbs.append(data)
    data = {
    "ID": 5,
    "verb": "north"
}
    verbs.append(data)
    data = {
    "ID": 5,
    "verb": "n"
}
    verbs.append(data)
    data = {
    "ID": 6,
    "verb": "s"
}
    verbs.append(data)
    data = {
    "ID": 6,
    "verb": "south"
}
    verbs.append(data)
    data = {
    "ID": 7,
    "verb": "west"
}
    verbs.append(data)
    data = {
    "ID": 7,
    "verb": "w"
}
    verbs.append(data)
    data = {
    "ID": 8,
    "verb": "e"
}
    verbs.append(data)
    data = {
    "ID": 8,
    "verb": "east"
}
    verbs.append(data)
    data = {
    "ID": 9,
    "verb": "exam"
}
    verbs.append(data)
    data = {
    "ID": 9,
    "verb": "examine"
}
    verbs.append(data)
    data = {
    "ID": 10,
    "verb": "wear"
}
    verbs.append(data)
    data = {
    "ID": 11,
    "verb": "remove"
}
    verbs.append(data)
    data = {
    "ID": 12,
    "verb": "get"
}
    verbs.append(data)
    data = {
    "ID": 12,
    "verb": "take"
}
    verbs.append(data)
    data = {
    "ID": 13,
    "verb": "drop"
}
    verbs.append(data)
    data = {
    "ID": 14,
    "verb": "use"
}
    verbs.append(data)
    data = {
    "ID": 15,
    "verb": "read"
}
    verbs.append(data)
    data = {
    "ID": 16,
    "verb": "dig"
}
    verbs.append(data)
    data = {
    "ID": 17,
    "verb": "climb"
}
    verbs.append(data)
    data = {
    "ID": 18,
    "verb": "verbose"
}
    verbs.append(data)
    data = {
    "ID": 19,
    "verb": "brief"
}
    verbs.append(data)
    data = {
    "ID": 20,
    "verb": "open"
}
    verbs.append(data)
    data = {
    "ID": 21,
    "verb": "close"
}
    verbs.append(data)
    data = {
    "ID": 22,
    "verb": "clear"
}
    verbs.append(data)
    data = {
    "ID": 0,
    "verb": "quit"
}
    verbs.append(data)
    
    data = {
    "ID": 1,
    "verb": "instructions"
}
    verbs.append(data)

    data = {
    "ID": 23,
    "verb": "exits"
}
    verbs.append(data)

    data = {
    "ID": 23,
    "verb": "directions"
}
    verbs.append(data)
    
def parser(string_to_parse):
    #splits the input into verb and noun
    if not string_to_parse:
        #returns to prompt if no input
        return
    noun=""
    noun_tmp=""
    string_to_parse=string_to_parse.lower() #convert the user input to lower case for easy comparison
    #remove the from string
    string2=string_to_parse.replace(' the '," ") #remove all occurences of 'the'
    string3=string2.replace(' a '," ") #remove all occurences of 'a'
    string_to_parse=string3.replace(' an '," ") #remove all occurences of 'an'
    x=string_to_parse.split(" ",1) #split into max two list-items
    no_of_word=len(x) #how many words are there. Item two may be several words
    verb=x[0] #the verb is the first item
    if no_of_word==2:
        noun_tmp=x[1]
        space=noun_tmp.find(" ") #are there any remaining spaces in the input?
        if space == -1: #no, there is not
            noun=noun_tmp
        else:
            for i in noun_tmp:
                if i==" ":
                    break #break out of loop when a space is detected
                noun=noun+i #add the noun letter by letter to the variable
    else:
        noun="None" #sets if there was only word entered, i.e. inventory
    return verb,noun

def check_input(verb,noun,name):
    if verb not in verbset:
        print(f"I'm sorry {name}, I do not understand that verb.")
        #f"{name}, what is thy bidding? "
        return
    
    for i in range(len(verbs)):
        curr_verb=verbs[i]
        array_verb=curr_verb['verb']
        array_id=curr_verb['ID']
        if verb==array_verb:
            #break out of the loop when typed verb corresponds to entry in combined list/dict
            #synonyms have the same ID. That way one case statement can match as many synonyms as you want without a lot of repeated code
            break
        
    match array_id:
        case 0:             #quit
            return 50       #exit game from main-py. Will also be returned if player dies
        case 1:             #help
            print_instructions()
        case 2:             #verbs
            print_verbs()
        case 3:             #look
            print_location(current_location,1)
        case 4:             #inventory
            inventory()
        case 7:             #go west
            go_west()
        case 22:                #clear
            os.system("cls")    #clears the console
        case 18:                #verbose
            set_verbose()
        case 19:                #brief
            set_brief()
        case 23:                #exits
            print_direction(current_location)
def create_locations ():
    data = {
    "brief": "You are in limbo.",
    "verbose": "You're in limbo. Everything is as dark as one would expect of the afterlife. Sorry dear, you're dead.",
    # Essentially here to make sure the map really starts at 1. 
    # In "Pirate Island" it is impossible for the player to die so this will never be displayed
    # However, the code is getting flexible enough so any if-game could potentially be developed using this code
    # If another game was developed using this code as the base, the player could be "transported" here when they die
    # before showing the end-of-game message
    "outdoors": False,
    "visited": False,
    "east": 0,
    "west": 0,
    "south": 0,
    "north": 0
}
    locations.append(data)

    data = {
    "brief": "You are at the bottom of a cliff.",
    "verbose": "You are at the bottom of a steep cliff. The very rock is as vertical as it can get, and you don't fancy looking up since the very thought of it is making you nauseous. There is a rope to be climbed back up, allowing for the nausea.",
    "outdoors": True,
    "visited": False,
    "east": 0,
    "west": 0,
    "south": 5,
    "north": 0
}
    locations.append(data)
    
    data = {
    "brief": "You are the top of a cliff.",
    "verbose": "You're at the top of a cliff. Far, far down below you can see a path dwindling south towards what seems to be a harbour. There is a huge piece of rock jutting out of what looks to be granite, although you can not be sure. You are, after all, a pirate and not a geologist. ",
    "outdoors": True,
    "visited": False,
    "east": 0,
    "west": 0,
    "south": 6,
    "north": 0
}
    locations.append(data)
    
    data = {
    "brief": "You are at a beach.",
    "verbose": "You're at beach at the northern end of this rather small island. The ground is uneven and there are plenty of rocks of various sizes strewn around, making you quite happy that you are wearing quite sturdy boots.",
    "outdoors": True,
    "visited": False,
    "east": 4,
    "west": 0,
    "south": 7,
    "north": 0
}
    locations.append(data)
    
    data = {
    "brief": "You are at a beach.",
    "verbose": "You're at beach at the north-eastern end of this somewhat small island. In the water you can see several fishes swimming by and doing whatever fishes usually do. The sand is kinda golden in look, and is soft to the touch.",
    "outdoors": True,
    "visited": False,
    "east": 0,
    "west": 3,
    "south": 8,
    "north": 0
}
    locations.append(data)
    
    data = {
    "brief": "You are at the shore.",
    "verbose": "You're at the shore. It is more of a harbour really, with one sole ship lying anchored here. The ship is somewhat small, but appears to be sea-worthy. A grim-looking guard watches the entry with a stern look in his eyes.",
    "outdoors": True,
    "visited": False,
    "east": 0,
    "west": 0,
    "south": 18,
    "north": 1
}
    locations.append(data)
    
    
    
    data = {
    "brief": "You are in the jungle.",
    "verbose": "You're at the edge of the jungle. Birds are chirping, and the jungle is not as thick here. Which is good, since that means there are fewer places for dangerous animals to hide.",
    "outdoors": True,
    "visited": False,
    "east": 7,
    "west": 0,
    "south": 0,
    "north": 2
}
    locations.append(data)

    data = {
    "brief": "You are in a small clearing.",
    "verbose": "You're in a clearing. In the trees surrounding the clearing you can see some monkeys monkeying around. Paths lead off in all directions, although the path running to the east is blocked by a large chest.",
    "outdoors": True,
    "visited": False,
    "east": 0,
    "west": 6,
    "south": 11,
    "north": 3
}
    locations.append(data)

    return current_location

def print_verbs(): 
    print("The game understands the following verbs (including abreviations): \n")
    for verb in verbset:
        print_yellow(verb.capitalize())

def print_location(which_location,verbose_mode):
    current_location_data=locations[which_location]
    
    brief=current_location_data['brief']
    verbose=current_location_data['verbose']
    outdoors=current_location_data['outdoors']
    visited=current_location_data['visited']
    #the if statement checks whether vebose-mode has been turned on, you've never visted that location before, or you used the look-verb to redisplay the location
    if verbosity==True or visited==False or verbose_mode==1:
        print(verbose)
    else:
        print(brief)
    
    print_direction(which_location)
    current_location_data['visited']=True   #the location has now been visited
    you_can_see()
    

def print_direction(where):
    print("\nYou can go: ",end = " ")
    mydirs=""
    current_location_data=locations[where]
    east=current_location_data['east']
    west=current_location_data['west']
    south=current_location_data['south']
    north=current_location_data['north']
    if east==0 and west==0 and south==0 and north==0:
        mydirs="Nowhere!"
    if east>0:
        mydirs=mydirs+"East "
    if west>0:
        mydirs=mydirs+"West "
    if south>0:
        mydirs=mydirs+"South "
    if north>0:
        mydirs=mydirs+"North"
    
    print_green(mydirs)
    
def set_verbose():
    global verbosity
    verbosity=True
    print("Verbose mode ON")

def set_brief():
    global verbosity
    verbosity=False
    print("Verbose mode OFF")

def inventory():
    print("You are carrying:")
    inventory=0     #Keep track of how much you are carrying
    
    for item in objects:
        
        locat=item['location']
        
        if locat==-1:
            print_yellow(item['description'])
            inventory+=1
    
    if inventory==0:
        print_red("Bloody nothing!")

def you_can_see():
    
    see_string=""
    location_see=0 # keep track of local objects
    for item in objects:
        locat=item['location']
        if item['visible']==False:
            #skip items that should not be shown
            continue
        if locat==current_location:
            #print(" "+item['description'],end = " ")
            see_string=see_string+" "+item['description']
            location_see+=1
    
    if location_see>0:
        print("You can see:",end = " ")
        print(see_string)
            
def go_west():
    global current_location
    current_location_data=(locations[current_location])
    west=current_location_data['west']
    if west==0:
        print("You can not go that way!")
    else:
        current_location=west
        print_location(current_location,0)
        
    