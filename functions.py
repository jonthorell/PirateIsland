"""
Initial declarations in functions.py
"""
import os

os.system("")  # enables ansi escape characters in terminal
os.system("cls")  # clears the console

COLOR = {
    # used by the print_green etc functions to refer to the color by name.
    # ENDC is used to go back to default
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "CYAN": "\033[96m",
    "YELLOW": "\033[93m",
    "ENDC": "\033[0m",
}

# verbset is used to easy make a "I do not know that verb" error.
# If the verb is not in this set it can not be used by the player.
# It is a set to make sure there are no duplicate values

verbset = {
    "exit",
    "l",
    "help",
    "verbs",
    "look",
    "i",
    "inventory",
    "n",
    "north",
    "s",
    "south",
    "w",
    "west",
    "e",
    "east",
    "exam",
    "examine",
    "wear",
    "remove",
    "get",
    "take",
    "drop",
    "use",
    "read",
    "down",
    "up",
    "verbose",
    "brief",
    "open",
    "break",
    "clear",
    "quit",
    "instructions",
    "exits",
    "directions",
    "investigate",
    "hint",
    "d",
    "u",
}

# lists used to keep track of locations, nouns, etc. These have the
# potential to change during the game.

locations = []
objects = []
verbs = []
nouns = []

current_location = 14  # start-location
verbosity = False
# True=always print verbose text, False only at first visit. Altered by
# verbose and brief functions
# The variables current_location and verbosity are used in so many places
# (and in functions called by other functions as well) so it made most sense
# to have them as globals.
# They are not updated in many places so is relatively risk-free

# The project does not rely on external libraries/frameworks so the
# risk of variable-clash is none

# Some functions to print text in different colors


def print_green(text):
    """
    Print text in green, from constant COLOR
    """
    print(COLOR["GREEN"], text, COLOR["ENDC"])


def print_header(text):
    """
    Print text in header, from constant COLOR
    """
    print(COLOR["HEADER"], text, COLOR["ENDC"])


def print_blue(text):
    """
    Print text in blue, from constant COLOR
    """
    print(COLOR["BLUE"], text, COLOR["ENDC"])


def print_red(text):
    """
    Print text in red, from constant COLOR
    """
    print(COLOR["RED"], text, COLOR["ENDC"])


def print_cyan(text):
    """
    Print text in cyan, from constant COLOR
    """
    print(COLOR["CYAN"], text, COLOR["ENDC"])


def print_yellow(text):
    """
    Print text in yellow, from constant COLOR
    """
    print(COLOR["YELLOW"], text, COLOR["ENDC"])


def parser(string_to_parse):
    """
    Splits user input into verb and noun
    """
    # splits the input into verb and noun
    if not string_to_parse:
        # returns to prompt if no input
        return
    noun = ""
    noun_tmp = ""  # noun and noun_tmp empty strings at first
    string_to_parse = (
        string_to_parse.lower()
    )  # convert the user input to lower case for easy comparison
    # remove the, a, and an from string. To make sure player can
    # write stuff like "open the door" if one wants to despite that
    # the game is verb-noun only based

    string2 = string_to_parse.replace(" the ", " ")  # remove 'the'
    string3 = string2.replace(" a ", " ")  # remove 'a'
    string_to_parse = string3.replace(" an ", " ")  # remove 'an'

    x = string_to_parse.split(" ", 1)  # split into max two list-items
    # how many words are there. Item two may be several words
    no_of_word = len(x)
    verb = x[0]  # the verb is the first item
    if no_of_word == 2:
        noun_tmp = x[1]  # noun_tmp is the second "word". Word may be several
        # are there any remaining spaces in the input?
        space = noun_tmp.find(" ")
        if space == -1:  # no, there is not
            noun = noun_tmp
        else:
            # iterate thru noun_tmp letter by letter until a space is detected.
            # To make sure the noun is one word only. The rest is discarded
            for i in noun_tmp:
                if i == " ":
                    break  # break out of loop when a space is detected
                noun += i  # add the noun letter by letter to the variable
    else:
        noun = "None"  # sets if there was only word entered, i.e. inventory
    return verb, noun


def check_input(verb, noun, name):
    """
    Check if the input is valid. Parser 2 if you will. When an id has
    been found, jump to the corresponding function.
    """
    if verb not in verbset:
        print_red(f"I'm sorry {name}, I do not understand that verb.")
        return
    for i in range(len(verbs)):
        # loop thru the list verbs to get the id of the verb used
        array_id = verbs[i]["ID"]
        if verb == verbs[i]["verb"]:
            # break out of the loop when typed verb corresponds to entry in
            # combined list/dict. synonyms have the same ID. That way one
            # case statement can match as many synonyms as you want without
            # a lot of repeated code thanks to the 'if verb not in verbset'
            # at the top, there is no need for an else. Sooner or later,
            # this if-statement will return true
            break
    match array_id:
        # array_id corresponds to the verb_id. Depending on the id, jump to
        # the corresponding function
        case 0:  # quit
            return 50  # exit game from main-py.
        case 1:  # help
            print_instructions()
        case 2:  # verbs
            print_verbs()
        case 3:  # look
            # the 1 in arguments is to make sure the verbose text is always
            # displayed when using 'look'
            print_location(1)
        case 4:  # inventory
            inventory()
        case 5:  # go north
            go_north()
        case 6:  # go south
            go_south()
        case 7:  # go west
            go_west()
        case 8:  # go east
            go_east()
        case 9:  # examine something
            examine(noun)
        case 10:  # wear something
            wear(noun)
        case 11:  # remove something
            remove(noun)
        case 12:  # get something
            get(noun)
        case 13:  # drop something
            drop(noun)
        case 14:  # use
            use(noun)
        case 15:  # read
            read(noun)
        case 16:  # go down
            go_down()
        case 17:  # go up
            go_up()
        case 18:  # verbose
            set_verbose()
        case 19:  # brief
            set_brief()
        case 20:  # open
            v_open(noun)
        case 21:  # break
            v_break(noun)
        case 22:  # clear
            os.system("cls")  # clears the console
        case 23:  # exits
            print_direction()
        case 24:
            hint()  # prints a small hint
        case _:  # default. Should never happen. Here as a failsafe.
            raise SystemExit("An unexpected error happened. Sorry about that")


def print_verbs():
    """
    Function print_verbs() prints out the available verbs
    """
    pr_str = "The game understands the following verbs (including "
    pr_str += "abreviations): \n"
    print(pr_str)
    for verb in verbset:
        print_yellow(verb.capitalize())


def print_location(verbose_mode):
    """
    Function print_location() displays the current location
    """
    brief = locations[current_location]["brief"]
    verbose = locations[current_location]["verbose"]
    outdoors = locations[current_location]["outdoors"]
    visited = locations[current_location]["visited"]
    # the if statement checks whether vebose-mode has been turned on,
    # you've never visted that location before, or you used the
    # look-verb to redisplay the location
    if verbosity is True or visited is False or verbose_mode == 1:
        print(verbose)
    else:
        print(brief)

    print_direction()  # print "You can go:"
    locations[current_location]["visited"] = True
    # the location has now been visited
    you_can_see()  # print "You can see:"


def print_direction():
    """
    Function print_direction() prints out the directions the player can go
    """
    print("\nYou can go: ", end=" ")
    # end=" ", make sure there is no linebreak
    mydirs = ""  # empty to start with

    # get the value for the different directions
    east = locations[current_location]["east"]
    west = locations[current_location]["west"]
    south = locations[current_location]["south"]
    north = locations[current_location]["north"]
    up = locations[current_location]["up"]
    down = locations[current_location]["down"]
    # Add the different locations to the string
    if east > 0:
        mydirs += "East "
    if west > 0:
        mydirs += "West "
    if south > 0:
        mydirs += "South "
    if north > 0:
        mydirs += "North "
    if down > 0:
        mydirs += "Down "
    if up > 0:
        mydirs += "Up "
    if mydirs == "":
        mydirs = "Nowhere!"  # replace the entire string if you can go nowhere
    print_green(mydirs)


def set_verbose():
    """
    Function set_verbose() turns on verbose mode. That is, always
    print long description
    """
    global verbosity
    verbosity = True
    print("Verbose mode ON")


def set_brief():
    """
    Function set_brief() turns of verbose mode. Print the long
    description on first visit or when using the verb look
    """
    global verbosity
    verbosity = False
    print("Verbose mode OFF")


def inventory():
    """
    Function inventory() lists what the player is carrying
    """
    print("You are carrying:")
    inventory = 0  # Keep track of how much you are carrying
    for item in objects:
        if item["location"] == -1:  # where is the object?
            # print the object if the player is carrying it
            print_yellow(item["description"])
            inventory += 1
    if inventory == 0:
        print_red(
            "Bloody nothing!"
            # since you can not drop the eyepatch, this will never be
            # shown. Just there in case one wants to expand the game or
            # use it as a basis for another
        )


def you_can_see():
    """
    Function you_can_see() lists objects visible at the current location
    """
    # used to print "You can see:" at the end of the location
    see_string = ""  # empty at first
    location_see = 0  # keep track of local objects
    for item in objects:
        if item["visible"] is False:
            # skip items that should not be shown
            continue
        if item["location"] == current_location:
            # if the object is located where the player is, add the
            # object to the see_string
            see_string += " " + item["description"]
            location_see += 1  # add one to variable
    if location_see > 0:
        # if location_see>0 that means something should be displayed.
        # That is, something is visible and at the current location
        print("You can see:", end=" ")  # no linebreak
        print_green(see_string)


def go_west():
    """
    Function go_west() moves the player westwards if possible
    """
    global current_location
    west = locations[current_location]["west"]
    if west <= 0:
        print("You can not go that way!")
    else:
        current_location = west
        print_location(0)
        # the zero is there to make sure the verbose/brief
        # setting is adhered to


def go_east():
    """
    Function go_east() moves the player eastwards if possible
    """
    global current_location
    east = locations[current_location]["east"]
    if east <= 0:
        print("You can not go that way!")
    else:
        current_location = east
        print_location(0)
        # the zero is there to make sure the verbose/brief
        # setting is adhered to


def go_north():
    """
    Function go_north() moves the player northwards if possible
    """
    global current_location
    north = locations[current_location]["north"]
    if north <= 0:
        print("You can not go that way!")
    else:
        current_location = north
        print_location(0)
        # the zero is there to make sure the verbose/brief
        # setting is adhered to


def go_south():
    """
    Function go_south() moves the player southwards if possible
    """
    global current_location
    south = locations[current_location]["south"]
    if south <= 0:
        print("You can not go that way!")
    elif current_location == 5 and south == 18:
        guard = "The guard steps infront of you and says "
        guard += "\"And where do you think you are\ntrying to "
        guard += "go mi-laddio? This is private property!\""
        print(guard)
        # when guard has been bribed, value of south has been changed
        # so this won't show up
    else:
        current_location = south
        print_location(0)
        # the zero is there to make sure the verbose/brief
        # setting is adhered to


def go_up():
    """
    Function go_up() moves the player upwards if possible
    """
    global current_location
    up = locations[current_location]["up"]
    if up <= 0:
        print("You can not go that way!")
    else:
        current_location = up
        print_location(0)
        # the zero is there to make sure the verbose/brief
        # setting is adhered to


def go_down():
    """
    Function go_down() moves the player downwards if possible
    """
    global current_location
    down = locations[current_location]["down"]
    if down <= 0:
        print("You can not go that way!")
    else:
        current_location = down
        print_location(0)


def hint():
    """
    Function hint() provides some hints at some locations
    """
    if current_location == 15 and locations[current_location]["east"] != 16:
        # if the door has not been opened, provide a hint
        print("You may want to find a way to open that door.")
    elif current_location == 7 and objects[20]["visible"] is False:
        # if the key is "invisible" the chest has not been opened
        print("There might something special about that chest.")
    elif current_location == 2 and locations[current_location]["down"] == 0:
        # if down=0, the path down has not been revealed
        print("You may want to find a way of climbing down the cliffside.")
    elif current_location == 8 and locations[current_location]["south"] == 0:
        # if south=0, then the gate has not been broken
        print("The gate is in the way. How can that be solved?")
    elif current_location == 5 and locations[current_location]["south"] == 18:
        # if south=18, then the guard hasn't been bribed yet
        print("You want to get rid of the guard somehow.")
    elif current_location == 17:
        print("Remember, X marks the spot.")
    else:
        print("I have no hint to provide at this time.")


def wear(noun):
    """
    Function wear() lets the player wear some things
    """
    result = get_noun_by_id(noun)
    match = result[0]
    error = requires_noun(noun)
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        print_red('How am I supposed to wear that?! What is a "' + noun + '"?')
        return
    else:
        noun_id = result[1]
    if noun_id == 10:
        if objects[noun_id]["location"] == -1:
            # you are carrying the ring
            dead_str = "\nOh no! The ring was cursed and turned you "
            dead_str += "into a gold-statue."
            print("You put the ring on your finger.")
            dead(dead_str)
        if (
            objects[noun_id]["location"] == current_location
            and objects[noun_id]["visible"] is True
        ):
            # the ring is visble but not carried
            print("You pick up the ring and put it on your finger.")
            dead_str = "\nOh no! The ring was cursed and turned you "
            dead_str += "into a gold-statue."
            dead(dead_str)
    if noun_id != 3:
        # in case player tries to wear something besides the eyepatch
        print("How am I supposed to wear that?")
    else:
        print("But you are already wearing it.")


def remove(noun):
    """
    Function remove() is the opposite of wear(). Lets the
    player unwear something
    """
    result = get_noun_by_id(noun)
    match = result[0]
    error = requires_noun(noun)
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        error = "Que? I can't see how I'm gonna remove that."
        error += ' What is a "' + noun + '"?"'
        print_red(error)
        return
    else:
        noun_id = result[1]
    if noun_id != 3:
        print("Que? I can't see how I'm gonna remove that.")
    else:
        print("And ruin that piratey-look? I think not!")


def dead(text):
    """
    Function dead() is used to display some game-over text when the
    player dies, and promtly exit the game
    """
    print_red(text)
    raise SystemExit("You have failed.")


def read(noun):
    """
    Function read() lets the player read some things
    """
    result = get_noun_by_id(noun)
    match = result[0]
    error = requires_noun(noun)
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        error = "I'm sorry, I do not know how to read that."
        error += ' What is a "' + noun + '"?'
        print_red(error)
        return
    else:
        noun_id = result[1]
    if noun_id == 6:
        # read paper
        if objects[noun_id]["location"] != -1:
            print("But you do not have a piece of paper.")
        else:
            finish = "The piece of paper is both a map of the sea as well "
            finish += "as instructions on\nhow to operate the ship."
            finish += "\n\nNow you can finally get home to do "
            finish += "some more pirating!"
            print_blue(finish)
            raise SystemExit("\nWell done! You have completed the game!")
    elif noun_id == 11 and current_location == 13:
        print('The writing on the board says: "Beware of cannibals". Yikes!')
    else:
        print("I'm sorry, I do not know how to read that.")


def v_break(noun):
    """
    Function v_break() (v_ is there avoid conflict with reserved key-word)
    lets the player break/smash some things
    """
    result = get_noun_by_id(noun)
    match = result[0]
    error = requires_noun(noun)
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        error = "Que? I can't see how I'm gonna break that."
        error += ' What is a "' + noun + '"?'
        print_red(error)
        return
    else:
        noun_id = result[1]
    if noun_id == 2:
        if (
            objects[noun_id]["location"] == -1
            or objects[noun_id]["location"] == current_location
        ):
            # is the bottle either carried or at the current location?
            if objects[4]["visible"] is True:
                # has the map been found?
                print("But the bottle has already been smashed.")
            else:
                # update objects
                pr_str = "You smash the bottle and can "
                pr_str += "retrieve the piece of paper."
                pr_str += "\nIt turns out to be a map!"
                print(pr_str)
                objects[4]["visible"] = True
                objects[4]["location"] = current_location
                objects[noun_id]["description"] = "a broken bottle"
                objects[noun_id]["exam"] = "The bottle is broken."
        return
    if (
        current_location == 8
        and locations[current_location]["south"] == 0
        and noun_id == 19
    ):
        # break gate
        # if south=0, unbroken
        pr_str = "Apparently, the bars of the gate were made "
        pr_str += "out of styrofoam so the\ngate is easily broken."
        print(pr_str)
        # update dicts
        locations[current_location]["south"] = 12
        new_verbose = "You're at the bottom of a hill. "
        new_verbose += "Sometime in the past someone made an artificial "
        new_verbose += "cave in it, and the entrence is to the south."
        locations[current_location]["verbose"] = new_verbose
        objects[noun_id]["exam"] = "Some vandal has broken the gate."
    elif (
        current_location == 8
        and locations[current_location]["south"] == 12
        and noun_id == 19
    ):
        print("But the gate has already been broken down.")
    elif current_location == 15 and noun_id == 13:
        print("The door is way too sturdy for that.")
    else:
        print("Que? I can't see how I'm gonna break that.")


def get_noun_by_id(noun):
    """
    Function get_noun_by_id() finds the id of the noun the player
    typed and returned back to the calling function, where it is
    used in if-else caulses to see if what the player tried to do
    makes sense
    """
    match = 0  # initial value. If still 0 at end of loop, no match
    for i in range(len(nouns)):
        curr_noun = nouns[i]
        array_noun = curr_noun["noun"]
        array_id = curr_noun["ID"]
        if array_noun == noun:
            match = 1
            return match, array_id
    return match, array_id


def get(noun):
    """
    Function get() lets the player pick up objects
    """
    result = get_noun_by_id(noun)
    match = result[0]
    error = requires_noun(noun)
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        error = "I'm sorry, I do not know how to pick that up. "
        error += 'What is a "' + noun + '"?'
        print_red(error)
        return
    else:
        noun_id = result[1]
    if objects[noun_id]["location"] == -1:
        print("But you are already carrying it.")
    elif (
        objects[noun_id]["location"] == current_location
        and objects[noun_id]["gettable"] is True
        and objects[noun_id]["visible"] is True
    ):
        # only pick up the object if:
        # 1. It is in the current location,
        # 2. It is gettable, and
        # 3. It is marked as visible.
        print("You pick up " + objects[noun_id]["description"] + ".")
        objects[noun_id]["location"] = -1
    elif current_location == 7 and noun_id == 1:
        print("It is far too heavy to pick up!")
    elif (
        current_location == 15
        and noun_id == 13
        and objects[noun_id]["visible"] is True
    ):
        print("Why would you want to walk around with a heavy door for?")
    else:
        print("I'm sorry, I do not know how to pick that up.")


def drop(noun):
    """
    Function drop() lets the player drop objects
    """
    result = get_noun_by_id(noun)
    match = result[0]
    error = requires_noun(noun)
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        error = "I don't know how to drop that, mate."
        error += " What is a \"" + noun + '"?'
        print_red(error)
        return
    else:
        noun_id = result[1]
    if noun_id == 3:
        print("And ruin that piratey-look? I think not!")
    elif objects[noun_id]["location"] != -1:
        print("But that is not something you have in your possession, mate.")
    elif objects[noun_id]["location"] == -1:
        # Drop the object.
        print("You drop " + objects[noun_id]["description"] + ".")
        objects[noun_id]["location"] = current_location
    else:
        print(
            "I'm sorry, I do not know how to drop that."
        )  # should never happen. Here as a fail-safe


def v_open(noun):
    """
    Function v_open() (v_ to avoid clash with built in key-word) lets the
    player open certain things
    """
    result = get_noun_by_id(noun)
    match = result[0]
    error = requires_noun(noun)
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        error = "I don't know how to open that, mate. "
        error += "What is a \"" + noun + '"?'
        print_red(error)
        return
    else:
        noun_id = result[1]
    if current_location == 7 and noun_id == 1:
        if objects[20]["visible"] is False:
            pr_str = "With great effort, you open the chest."
            pr_str += "Inside it you find a small key."
            print(pr_str)
            objects[20]["visible"] = True
        else:
            print("But the chest is already open.")
    elif current_location == 15 and noun_id == 13:
        if locations[current_location]["east"] == 0:
            # east will be updated when the door is open
            print("The door is locked.")
        elif locations[current_location]["east"] == -1:
            pr_str = "You open the door. The hinges were bad "
            pr_str += "apparently so the door falls down onto "
            pr_str += "the ground."
            print(pr_str)
            locations[current_location]["east"] = 16
            new_verbose = "You are on the eastern end of the beach. "
            new_verbose += "It still looks lovely, but that old and"
            new_verbose += "worn-out house ruins the look. The door is open."
            locations[current_location]["verbose"] = new_verbose
            objects[noun_id]["visible"] = True
            objects[noun_id]["description"] = "a door on the ground"
        else:
            print("The door is already open.")
    else:
        print("I'm sorry, I don't know how to open that.")


def use(noun):
    """
    Function use() lets the player use certain objects. That can
    be say use sword to attack an enemy
    """
    global current_location
    result = get_noun_by_id(noun)
    match = result[0]
    error = requires_noun(noun)
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        error = "I don't know how to use that, mate."
        error += " What is a \"" + noun + '"?'
        print_red(error)
        return
    else:
        noun_id = result[1]
    if noun_id == 4:
        if objects[noun_id]["location"] != -1:
            # you can "use map" wherever you are
            # location-wise but you have to possess the map
            print("But you do not have a map.")
            return
        else:
            # if you have the map, "teleport" the
            # player to the treasure-site
            pr_str = "You use the map and when you followed "
            pr_str += "its instructions you are at..."
            print(pr_str)
            current_location = 17
            print_location(1)
            return
    # restart if-block since it is now using location as
    # primary identifyer. Mainly due to readability
    if current_location == 15 and noun_id == 20:
        # you can only use "use key" if you're in
        # location 15 (outside building)
        if objects[noun_id]["location"] != -1:
            # and if you possess they key
            print("But you don't have a key.")
        elif locations[current_location]["east"] == -1:
            # unneccesary to unlock twice
            print("But the door is already unlocked.")
        elif locations[current_location]["east"] == 16:
            # or when the door is open
            print("But the door is already opened.")
        else:
            # unlock the door
            pr_str = "You use the key to unlock the door."
            pr_str += "\nIt could have used a wee bit of oil "
            pr_str += "beforehand, but it works."
            print(pr_str)
            locations[current_location]["east"] = -1
    elif current_location == 5 and noun_id == 21:
        # you can only "use treasure" if you're at the
        # shore with the escape-vessel
        if (
            objects[noun_id]["location"] != -1
            and locations[current_location]["south"] != 9
        ):
            # and you need to possess the treasure, and the
            # guard must not be bribed already
            print("But you do not have any treasure.")
        elif locations[current_location]["south"] == 9:
            # the guard has already been bribed. No need to do it twice.
            pr_str = "But the guard has already been bribed and "
            pr_str += "is nowhere to be seen."
            print(pr_str)
        else:
            pr_str = "The guard hesistantly accepts the "
            pr_str += "treasure as a bribe and wanders off."
            print(pr_str)
            locations[current_location]["south"] = 9
            # update the south direction so the guard
            # (not there anymore) does not stop you
            # from boarding the ship
            objects[noun_id]["location"] = 0
            # destroy the treausre so it is
            # no longer in your inventory
            objects[18]["location"] = 0
            # move the guard away from the scene
            # update the verbose description so the guard
            # is no longer displayed.
            new_verbose = "You're at the shore. It is more of a "
            new_verbose += "harbour really, with one sole ship lying "
            new_verbose += "\nanchored here. The ship is somewhat small, "
            new_verbose += "but appears to be sea-worthy."
            locations[current_location]["verbose"] = new_verbose
    elif current_location == 17 and noun_id == 14:
        # you need to be at the treasure-site to "use shovel"
        if objects[noun_id]["location"] != -1:
            # you need to possess the shovel
            print("But you do not have a shovel.")
        elif objects[21]["visible"] is True:
            # and you can not find the treasure twice
            print("But you have already found the treasure.")
        else:
            pr_str = "You dig furiously for several hours, and is"
            pr_str += " rewarded when you find\na huge buried treasure."
            print(pr_str)
            objects[21]["visible"] = True  # reveal the treasure
    elif current_location == 2 and noun_id == 8:
        # you can only "use rope" at location 2 (top of cliff)
        if locations[current_location]["down"] == 1:
            # if you haven't used the rope already that is
            print("But you have already used the rope.")
        elif objects[noun_id]["location"] != -1:
            # and you need to carry the rope
            print("But you do not have a rope.")
        else:
            pr_str = "You tie the rope around the rock "
            pr_str += "and let the other end run down the cliffside."
            print(pr_str)
            locations[current_location]["down"] = 1
            # make sure you can go down
            objects[noun_id]["location"] = 0
            # remove the rope from the inventory
            objects[noun_id]["gettable"] = False
            # you can not get the rope again
            objects[noun_id]["visible"] = False
            # the rope is made "invisible"
            # update the verbose description of the location

            new_verbose = "You're at the top of a cliff. Far, "
            new_verbose += "far down below you can"
            new_verbose += " see a path dwindling\nsouth towards "
            new_verbose += "what seems to be a harbour. There"
            new_verbose += " is a huge piece of rock jutting"
            new_verbose += "out of what looks to be granite"
            new_verbose += ", although you can not be sure."
            new_verbose += " You \nare, after all, a pirate "
            new_verbose += "and not a geologist."
            new_verbose += " A piece of rope is \ntied to the rock."
            locations[current_location]["verbose"] = new_verbose
    else:
        print("I don't know how to use that.")


def examine(noun):
    """
    Function examine() lets the player examine or investigate certain
    objects in further detail
    """
    result = get_noun_by_id(noun)
    match = result[0]
    error = requires_noun(noun)
    if error:
        return
        # if error is true, no noun was entered. Return to prompt
    if match == 0:
        error = "I don't know how to examine that, mate."
        error += 'What is a "' + noun + '"?'
        print_red(error)
        return
    else:
        noun_id = result[1]

    # check conditionals
    if current_location == 9 and noun_id == 5:
        # skeleton
        if objects[6]["visible"] is False:
            pr_str = "When you examine what remains of the skeletons"
            pr_str += "clothing, you\ndiscover a piece of paper and "
            pr_str += "an ID-card."
            print(pr_str)
            objects[6]["visible"] = True
            objects[7]["visible"] = True
            return
        else:
            print(objects[noun_id]["exam"])
            return
    elif current_location == 13 and noun_id == 22:
        # banana
        print(objects[noun_id]["exam"])
    elif current_location == 4 and noun_id == 23:
        # sand
        print(objects[noun_id]["exam"])
    elif current_location == 1 and noun_id == 8:
        # rope at bottom of cliff
        pr_str = "A long rope made of the finest Hithlain. Elven-made when"
        pr_str += "\nelves still roamed middle-earth. There is no way to "
        pr_str += "get it back."
        print(pr_str)
        return
    elif current_location == 2 and noun_id == 8:
        # rope tied to cliff
        # need a special condition here since the rope can sometimes be
        # examined without being in your possession
        if locations[current_location]["down"] == 1:
            # if rope has been used
            pr_str = "A long rope made of the finest Hithlain. Elven-made when"
            pr_str += "\nelves still roamed middle-earth. There is no way to "
            pr_str += "get it back.\nIt is tied too "
            pr_str += "securely to the cliff for that."
            print(pr_str)
            return
        if objects[noun_id]["location"] == -1:
            # rope being carried
            print(objects[noun_id]["exam"])
        elif objects[noun_id]["location"] == current_location:
            # rope is at location
            print(objects[noun_id]["exam"])
        else:
            # rope not used, carried, or at location
            print_red("I'm sorry, I can not examine that.")
    elif current_location == 3 and noun_id == 17:
        # rocks
        if objects[10]["visible"] is False:
            # when the ring has not been found yet
            objects[10]["visible"] = True  # has now been found
            print(objects[noun_id]["exam"])
        else:
            objects[noun_id][
                "exam"
            ] = "You found nothing out of the ordinary amongst the rocks."
            print(objects[noun_id]["exam"])
    elif current_location == 14 and noun_id == 15:
        # is the player by the ship and trying to exam it?
        print(objects[noun_id]["exam"])
    elif current_location == 13 and noun_id == 11:
        # board on bananatree
        print(objects[noun_id]["exam"])
    elif current_location == 13 and noun_id == 16:
        # tree
        print(objects[noun_id]["exam"])
    elif current_location == 15 and noun_id == 13:
        # door
        print(objects[noun_id]["exam"])
    elif current_location == 7 and noun_id == 1:
        # chest
        print(objects[noun_id]["exam"])
    elif current_location == 5 and noun_id == 18:
        # guard
        if objects[noun_id]["location"] != current_location:
            print("But the guard is not here.")
        else:
            print(objects[noun_id]["exam"])
    elif current_location == 8 and noun_id == 19:
        # gate
        print(objects[noun_id]["exam"])
    elif current_location == 12 and noun_id == 9:
        # table
        print(objects[noun_id]["exam"])
    elif current_location == 15 and noun_id == 12:
        # building
        print(objects[noun_id]["exam"])
    elif current_location == 5 and noun_id == 15:
        # vessel
        print("The ship is a luxury vessel to be sure!")
    elif objects[noun_id]["location"] == -1:
        # inventory, next to last because some exceptions can occur first
        print(objects[noun_id]["exam"])
    elif (
        objects[noun_id]["location"] == current_location
        and objects[noun_id]["visible"] is True
    ):
        # objects visible at current position, same as the inventory rule.
        print(objects[noun_id]["exam"])
    else:
        print_red("I'm sorry, I can not examine that.")


def print_instructions():
    """
    Function print_instructions() prints out the help-instructions. Printed
    at game-start and if the player types help
    """
    rules = "Interactive fiction is purely text-based, and can be considered"
    rules += "\na story where the player takes charge of the outcome rather "
    rules += "than\njust reading along. The player moves around in the game by"
    rules += " issuing\ncommands. These commands consists of one or two words,"
    rules += " in a\nverb-noun pattern.\n\n"
    rules += "Some verbs work on their own (inventory for example), others"
    rules += "\nneed a noun (open door for example).\n"
    rules += "\nThe idea is that you walk around in a fictional world and"
    rules += "\nsolves puzzles along the way. A puzzle can be (for example)"
    rules += "\nfinding the key to a locked door so it can be unlocked and the"
    rules += "\nplayer can get further into the world displayed."
    print_yellow(rules)
    input("Press Enter to continue...")
    rules = "A typical game is usually littered with information and objects "
    rules += "that \nthe player thinks might be important, but in the end "
    rules += "serves only as\ndistractions or red herrings."
    rules += "\n\nEverything after a second word will be discarded. "
    rules += "If you enter a\ncommand such as "
    rules += '"inventory list" and the verb (inventory) does not'
    rules += "\nexpect a noun, the noun will be discared as well.\n"
    rules += "\nDirections are always entered with just the direction."
    rules += "That is, \nit is a one-word sentence."
    rules += " Either 'north' or 'n' will suffice.\n"
    rules += "\nIn other words: everyting you need to do can be "
    rules += "accomplished by\neither a one or a "
    rules += "two-word command. Nothing fancier than that"
    rules += "\nis ever required.\n"
    print_yellow(rules)
    input("Press Enter to continue...")
    rules = "The first time you enter a location, you will get a long"
    rules += "\ndescription of the place. On subsequent visits you only"
    rules += "\nget a shorter one.\n"
    rules += "\nYou can get the long description again by issuing the"
    rules += '\ncommand "look". If you want to, you can change this to'
    rules += " \nalways describe the longer description.\n"
    rules += '\nYou do that by issueing the command "verbose".'
    rules += '\nTo revert to the default, issue the command "brief".\n'
    rules += "\nSome examples of commands (not specific to this game to"
    rules += "\navoid spoilers):\n"
    rules += "\nInventory: lists what you are carrying"
    rules += "\nExamine door: checks if there is something special "
    rules += "about the door."
    rules += "\nDepending on what you examine, other objects may be revealed."
    rules += "\nDrop book: drops the book into the current location"
    rules += "\nGet book: picks up the book, if it is available"
    rules += "\nOpen door: opens the door, if it can be opened"
    rules += "\nUse lamp: depends on the noun, but in this case it would turn"
    rules += "\non the lamp."
    print_yellow(rules)
    input("Press Enter to continue...")
    rules = "That should get you started."
    rules += "\nIf you need to, you can view these instructions again with"
    rules += "\nthe command help."
    rules += "\n\nAnd remember: read the descriptions carefully. They can"
    rules += " provide valueable clues."
    print_yellow(rules)


def requires_noun(noun):
    error = False
    if noun == "None" or noun == "":
        print_red("But this verb requires a noun!")
        error = True
    return error
