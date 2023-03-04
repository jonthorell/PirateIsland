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

verbset={"exit","l","help","verbs","look","i","inventory","n","north","s","south","w","west","e","east","exam","examine","wear","remove","get","take","drop","use","read","dig","climb","verbose","brief","open","break","clear","quit","instructions","exits","directions","investigate","hint"}
nounset={"sword","chest","bottle","eyepatch","map","skeleton","paper","id","rope","table","ring","board","building","door","shovel","ship","banana-tree","rocks","guard","gate","sign"}

locations=[]
objects=[]
verbs=[]
nouns=[]

current_location=14
verbosity=False
#True=always print verbose text, False only at first visit. Altered by verbose and brief functions

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
        return
        
    #if noun not in nounset:
    #    print(f"I'm sorry {name}, I do not understand that noun.")
    #    return    
    
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
        case 5:             #go north
            go_north()
        case 6:             #go south
            go_south()
        case 7:             #go west
            go_west()
        case 8:             # go east
            go_east()
        case 9:             #examine something
            examine(noun)
        case 10:                #wear something
            wear(noun)
        case 11:                #remove something
            remove(noun)
        case 12:                #get something
            get(noun)
        case 15:                #read
            read(noun)
        case 22:                #clear
            os.system("cls")    #clears the console
        case 18:                #verbose
            set_verbose()
        case 19:                #brief
            set_brief()
        case 21:                #break
            v_break(noun)
        case 23:                #exits
            print_direction(current_location)
        case 24:
            hint()              #prints a small hint

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
    if where==17:
        #do not display directions at treasure-site
        return
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
        
def go_east():
    global current_location
    current_location_data=(locations[current_location])
    east=current_location_data['east']
    if east==0:
        print("You can not go that way!")
    else:
        current_location=east
        print_location(current_location,0)
        
def go_north():
    global current_location
    current_location_data=(locations[current_location])
    north=current_location_data['north']
    if north==0:
        print("You can not go that way!")
    else:
        current_location=north
        print_location(current_location,0)
        
def go_south():
    global current_location
    current_location_data=(locations[current_location])
    south=current_location_data['south']
    if south==0:
        print("You can not go that way!")
    else:
        current_location=south
        print_location(current_location,0)  
        
def examine(noun):
    
    match=0    #initial value. If still 0 at end of loop, no match
    
    for i in range(len(nouns)):
        curr_noun=nouns[i]
        array_noun=curr_noun['noun']
        array_id=curr_noun['ID']
        if array_noun==noun:
            match=1
            break
    if match==0:
        print_red("Sorry, I don't understand what I should examine. What is a \""+noun+"\"?")
        return
    
    current_obj=objects[array_id]
    
    #print(current_location)
    #print(array_id)
    #print(current_obj)
    #print(noun)
    
    if current_location==9 and array_id==5:
        tmp_object=objects[6]
        if tmp_object['visible']==False:
            print("When you examine what remains of the skeletons clothing, you discover a piece of paper and an ID-card.")
            tmp_object['visible']=True
            tmp_object=objects[7]
            tmp_object['visible']=True
            return
        else:
            exam_text=current_obj['exam']
            print(exam_text)
            return
    
    if current_location==1 and array_id==8:
        #rope bottom of cliff
        exam_text="A long rope made of the finest Hithlain. Elven-made when elves still roamed middle-earth. There is no way to get it back."
        print(exam_text)
        return
    
    if current_location==3 and array_id==17:
        #rocks
        #should be in elif but does not work there. Here temporarily. WIll be moved to the elif construct eventually
        
        exam_text=current_obj['exam']
        tmp_object=objects[10]
        
        if tmp_object['visible']==False:
            #ring has not been discovered
            tmp_object['visible']=True
            current_obj['exam']="You found nothing out of the ordinary amongst the rocks."
        print(exam_text)
        return
    
    if current_obj['location']==-1:
        #first, check if player trying to examine something carried
        print(current_obj['exam'])
    elif current_obj['location']==current_location and current_obj['visible']==True:
        #check if object is at the current location and visible
        print(current_obj['exam'])
    elif current_location==14 and array_id==15:
        #is the player by the ship and trying to exam it?
        exam_text=current_obj['exam']
        print(exam_text)
    elif current_location==13 and array_id==11:
        #board on bananatree
        exam_text=current_obj['exam']
        print(exam_text)
    elif current_location==13 and array_id==16:
        #banana tree
        exam_text=current_obj['exam']
        print(exam_text)
    elif current_location==15 and array_id==12:
        #building
        exam_text=current_obj['exam']
        print(exam_text)
    elif current_location==15 and array_id==13:
        #door
        exam_text=current_obj['exam']
        print(exam_text)
    elif current_location==7 and array_id==1:
        #chest
        exam_text=current_obj['exam']
        print(exam_text) 
    elif current_location==5 and array_id==18:
        #guard
        exam_text=current_obj['exam']
        print(exam_text)
    elif current_location==8 and array_id==19:
        #gate
        exam_text=current_obj['exam']
        print(exam_text)
    elif current_location==12 and array_id==9:
        #table
        exam_text=current_obj['exam']
        print(exam_text)
    elif current_location==5 and array_id==15:
        exam_text="The ship is a luxury vessel to be sure!"
        print(exam_text)
    else:
        print_red("I'm sorry, I can not do that.")
    
    #"ID": 0,
    #"noun": "sword",
    #"description": "a cutlass sword",
    #"exam": "It is your typical cutlass. Nothing special about it, apart from some stains that appear to be blood.",
    #"location": -1,
    #"gettable": True,
    #"visible": True
    
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
    
    rules+="\n\nThe first time you enter a location, you will get a long description of the place. On subsequent visits you only get a shorter one."
    rules+="\nYou can get the long description again by issuing the command \"look\"."
    rules+="\nIf you want to, you can change this to always describe the longer description."
    rules+="\nYou do that by issueing the command \"verbose\"."
    rules+="\nTo revert to the default, issue the command \"brief\"."
    
    rules+="\n\nSome examples of commands (not specific to this game to avoid spoilers):"
    rules+="\nInventory: lists what you are carrying"
    rules+="\nExamine door - checks if there is something special about the door. Depending on what you examine, other objects may be revealed."
    rules+="\nDrop book - drops the book into the current location"
    rules+="\nGet book - picks up the book, if it is available"
    rules+="\nOpen door - opens the door, if it can be opened"
    rules+="\nUse lamp - depends on the noun, but in this case it would turn on the lamp."
    
    rules+="\n\nThat should get you started."
    rules+="\nIf you need to, you can view these instructions again with the command help."
    rules+="\n\nAnd remember: read the descriptions carefully. They can provide valueable clues."
    
    print_yellow(rules)
    
def hint():
    if current_location==15:
        print("You may want to find a way to open that door.")
    elif current_location==7:
        print("There might something special about that chest.")
    elif current_location==2:
        print("You may want to find a way of climbing down the cliffside.")
    elif current_location==8:
        print("The gate is in the way. How can that be solved?")
    elif current_location==5:
        print("You want to get rid of the guard somehow.")
    else:
        print("I have no hint to provide at this time.")
        
def wear(noun):
    if noun=="ring":
        tmp_object=objects[10]
        if(tmp_object['location']==-1):
            print("You put the ring on your finger.")
            dead("\nOh no! The ring was cursed and turned you into a gold-statue.")
        if tmp_object['location']==current_location and tmp_object['visible']==True:
            print("You pick up the ring and put it on your finger.")
            dead("\nOh no! The ring was cursed and turned you into a gold-statue.")
            
    if noun !="eyepatch":
        print("How am I supposed to wear that?")
    else:
        print("But you are already wearing it.")
        
def remove(noun):
    if noun !="eyepatch":
        print("Que? I can't see how I'm gonna remove that.")
    else:
        print("And ruin that piratey-look? I think not!")        

def dead(text):
    print_red(text)
    raise SystemExit('You have failed.')

def read(noun):
    result=get_noun_by_id(noun)
    match=result[0]
    if match==0:
        print("I'm sorry, I do not know how to read that.")
        return
    else:
        noun_id=result[1]
    
    #print("Outside of if: "+noun)
    if noun_id==11 and current_location==13:
        print("The writing on the board says: \"Beware of cannibals\". Yikes!")
    else:
        print("I'm sorry, I do not know how to read that.")
        
def v_break(noun):
    global current_location
    current_location_data=(locations[current_location])
    south=current_location_data['south']
    
    if current_location==8 and south==0 and noun=="gate":
        print("Apparently, the bars of the gate were made out of styrofoam so the gate is easily broken.")
        current_location_data['south']=12
        current_location_data['verbose']="You're at the bottom of a hill. Sometime in the past someone made an artificial cave in it, and the entrence is to the south."
        tmp_object=objects[19]
        tmp_object['exam']="Some vandal has broken the gate."
    elif current_location==8 and south==12 and noun=="gate":
        print("But the gate has already been broken down.")
    else:
        print("I don't know to break that.")
        
def get_noun_by_id(noun):
    match=0    #initial value. If still 0 at end of loop, no match
    
    for i in range(len(nouns)):
        curr_noun=nouns[i]
        array_noun=curr_noun['noun']
        array_id=curr_noun['ID']
        if array_noun==noun:
            match=1
            return match,array_id
    
    return match,array_id

def get(noun):
    result=get_noun_by_id(noun)
    match=result[0]
    if match==0:
        print("I'm sorry, I do not know how to pick that up.")
        return
    else:
        noun_id=result[1]
        print("Get id: "+str(noun_id))
    
    
    print("Outside of if: "+noun)
            
  
            
            