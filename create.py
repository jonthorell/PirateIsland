# This file creates all lists/dics necessary for the game

def createObjects(objects):
    """
    Function createObjetcs() create all the objetcs
    the player can interact with
    """
    # the different keys are for:
    # id: internal id to keep track of which object the user interacts with
    # noun: the noun used to refer to it.
    # description: Displayed in "You can see:" text at location
    # exam: what will be displayed when user examines the object
    # location: initial location. Updated when taken/dropped etc.
    # -1 if being carried
    # gettable: if the object can be taken or not.
    # visible: if the object should be displayed in "You can see:".
    # Used when something must be done before the object reveals itself.
    # Also used if something is being described in the main-text for objects
    # that are always in a specific location such as a building,
    # boat, etc

    exam = "It is your typical cutlass. Nothing special about it, apart"
    exam += " from some stains \nthat appear to be blood."

    data = {
        "ID": 0,
        "noun": "sword",
        "description": "a cutlass sword",
        "exam": exam,
        "location": -1,
        "gettable": True,
        "visible": True
    }
    objects.append(data)

    exam = "The chest looks and smells as if it is made out of campher wood."
    exam += " It looks like \nit is extremely heavy."

    data = {
        "ID": 1,
        "noun": "chest",
        "description": "a campher wood chest",
        "exam": exam,
        "location": 7,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "The bottle might have contained rum at one point. There seems"
    exam += " to be something\nelse inside it now, a piece of paper."

    data = {
        "ID": 2,
        "noun": "bottle",
        "description": "a dirty old bottle",
        "exam": exam,
        "location": 4,
        "gettable": True,
        "visible": True
    }
    objects.append(data)

    data = {
        "ID": 3,
        "noun": "eyepatch",
        "description": "an eyepatch (being worn)",
        "exam": "It is made of cloth, dyed black.",
        "location": -1,
        "gettable": True,
        "visible": True
    }
    objects.append(data)

    exam = "The paper the map is written on seems to be fragile. "
    exam += "Probably due\nto having been subjected to some liquid before."

    data = {
        "ID": 4,
        "noun": "map",
        "description": "a treasure map",
        "exam": exam,
        "location": 4,
        "gettable": True,
        "visible": False
    }
    objects.append(data)

    exam = "The skeleton is wearing what was once very nice clothes."
    exam += "Now the clothes\n"
    exam += "looks nothing like clothes, more like holes with remnants "
    exam += "of fabric around it."

    data = {
        "ID": 5,
        "noun": "skeleton",
        "description": "Mr skeleton",
        "exam": exam,
        "location": 9,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "The piece of paper is partially crumbled but"
    exam += "there are some words written on it."

    data = {
        "ID": 6,
        "noun": "paper",
        "description": "a piece of paper",
        "exam": exam,
        "location": 9,
        "gettable": True,
        "visible": False
    }
    objects.append(data)

    data = {
        "ID": 7,
        "noun": "id",
        "description": "a ID card",
        "exam": "Apparently the nobleman was called Murphy when he was alive.",
        "location": 9,
        "gettable": True,
        "visible": False
    }
    objects.append(data)

    exam = "A long rope made of the finest Hithlain."
    exam += " Elven-made when elves still roamed\nmiddle-earth."

    data = {
        "ID": 8,
        "noun": "rope",
        "description": "a long rope",
        "exam": exam,
        "location": 12,
        "gettable": True,
        "visible": True
    }
    objects.append(data)

    exam = "The table is made of balsa wood. No wonder it is unstable."
    exam += ' Someone has \ncarved "Smeagol was here" in it.'

    data = {
        "ID": 9,
        "noun": "table",
        "description": "an unstable table",
        "exam": exam,
        "location": 12,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "The ring is perfectly cirular with a huge"
    exam += " diamond decorating it."

    data = {
        "ID": 10,
        "noun": "ring",
        "description": "a golden ring",
        "exam": exam,
        "location": 3,
        "gettable": True,
        "visible": False
    }
    objects.append(data)

    exam = "What do you expect? It is a wooden board."
    exam += " However, there's some writing on it."

    data = {
        "ID": 11,
        "noun": "board",
        "description": "a wooden board",
        "exam": exam,
        "location": 13,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "The building seems to have been built using whatever could be "
    exam += "salvaged from\nvarious shipwrecks. Good craftsman skills of"
    exam += " whoever built it though"
    exam += " since it \nlooks like it could withstand anything."

    data = {
        "ID": 12,
        "noun": "building",
        "description": "a building",
        "exam": exam,
        "location": 15,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "The door is made out of metal, and there's"
    exam += " a small keyhole in it."

    data = {
        "ID": 13,
        "noun": "door",
        "description": "a door",
        "exam": exam,
        "location": 15,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "Just your ordinary treasure-hunting shovel."
    exam += " A must have for any \nrespectable pirate."

    data = {
        "ID": 14,
        "noun": "shovel",
        "description": "a small shovel",
        "exam": exam,
        "location": 16,
        "gettable": True,
        "visible": True
    }
    objects.append(data)

    exam = "The pirate vessel \"The Sea Monkey\" is too far out of your"
    exam += " reach to be \nexamined. You know it inside-out anyway."

    data = {
        "ID": 15,
        "noun": "ship",
        "description": "a pirate vessel",
        "exam": exam,
        "location": 14,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "The banana-tree is full of overripe bananas. They "
    exam += "look disgusting."

    data = {
        "ID": 16,
        "noun": "banana-tree",
        "description": "a banana-tree",
        "exam": exam,
        "location": 13,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "When you examine the rocks, you discover a"
    exam += " golden ring amongst them."
    exam += ' Could\nit be Sauron\'s fabled "One Ring"?'
    exam += "\n\nThat could really make this unfortunate"
    exam += " business of getting marooned\nto be worthwhile!"

    data = {
        "ID": 17,
        "noun": "rocks",
        "description": "a bunch of rocks",
        "exam": exam,
        "location": 3,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    data = {
        "ID": 18,
        "noun": "guard",
        "description": "a stern-looking guard",
        "exam": "No-one messes with Ace Rimmer!",
        "location": 5,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    data = {
        "ID": 19,
        "noun": "gate",
        "description": "a sturdy looking gate",
        "exam": "The gate is made up of 5 sturdy-looking bars.",
        "location": 8,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "The key seems to be made out of silver and some"
    exam += " other unknown ore. \nMithril maybe?"

    data = {
        "ID": 20,
        "noun": "key",
        "description": "a small key",
        "exam": exam,
        "location": 7,
        "gettable": True,
        "visible": False
    }
    objects.append(data)

    exam = "The treasure consists of gold, jewels, diamonds, sapphires, and"
    exam += " you name \nit. Worth many pieces of eights."

    data = {
        "ID": 21,
        "noun": "treasure",
        "description": "a huge treasure",
        "exam": exam,
        "location": 17,
        "gettable": True,
        "visible": False
    }
    objects.append(data)

    exam = "The bananas are very brown and looks inedible. Still,"
    exam += " they will\nprovide nourishment nonetheless."

    data = {
        "ID": 22,
        "noun": "banana",
        "description": "a banana",
        "exam": exam,
        "location": 13,
        "gettable": False,
        "visible": False
    }
    objects.append(data)

    exam = "The sand is made out of half sand and half gold!"

    data = {
        "ID": 23,
        "noun": "sand",
        "description": "golden sand",
        "exam": exam,
        "location": 4,
        "gettable": False,
        "visible": False
    }
    objects.append(data)


def createNouns(nouns):
    """
    Function createNouns() create all the words the user can use as a noun
    """
    # id field MUST correspond with the ID-field in objects.
    # Used for synonyms and determining which object the user
    # tries to manipulate
    data = {
        "ID": 0,
        "noun": "sword"
    }
    nouns.append(data)

    data = {
        "ID": 1,
        "noun": "chest"
    }
    nouns.append(data)

    data = {
        "ID": 2,
        "noun": "bottle"
    }
    nouns.append(data)

    data = {
        "ID": 3,
        "noun": "eyepatch"
    }
    nouns.append(data)

    data = {
        "ID": 4,
        "noun": "map"
    }
    nouns.append(data)

    data = {
        "ID": 5,
        "noun": "skeleton"
    }
    nouns.append(data)

    data = {
        "ID": 6,
        "noun": "paper"
    }
    nouns.append(data)

    data = {
        "ID": 7,
        "noun": "id"
    }
    nouns.append(data)

    data = {
        "ID": 8,
        "noun": "rope"
    }
    nouns.append(data)

    data = {
        "ID": 9,
        "noun": "table"
    }
    nouns.append(data)

    data = {
        "ID": 10,
        "noun": "ring"
    }
    nouns.append(data)

    data = {
        "ID": 11,
        "noun": "board"
    }
    nouns.append(data)

    data = {
        "ID": 12,
        "noun": "building"
    }
    nouns.append(data)

    data = {
        "ID": 13,
        "noun": "door"
    }
    nouns.append(data)

    data = {
        "ID": 14,
        "noun": "shovel"
    }
    nouns.append(data)

    data = {
        "ID": 15,
        "noun": "ship"
    }
    nouns.append(data)

    data = {
        "ID": 16,
        "noun": "banana-tree"
    }
    nouns.append(data)

    data = {
        "ID": 17,
        "noun": "rocks"
    }
    nouns.append(data)

    data = {
        "ID": 18,
        "noun": "guard"
    }
    nouns.append(data)

    data = {
        "ID": 19,
        "noun": "gate"
    }
    nouns.append(data)

    data = {
        "ID": 11,
        "noun": "sign"
    }
    nouns.append(data)

    data = {
        "ID": 3,
        "noun": "patch"
    }
    nouns.append(data)

    data = {
        "ID": 0,
        "noun": "cutlass"
    }
    nouns.append(data)

    data = {
        "ID": 16,
        "noun": "tree"
    }
    nouns.append(data)

    data = {
        "ID": 19,
        "noun": "gates"
    }
    nouns.append(data)

    data = {
        "ID": 19,
        "noun": "bar"
    }
    nouns.append(data)

    data = {
        "ID": 19,
        "noun": "bars"
    }
    nouns.append(data)

    data = {
        "ID": 20,
        "noun": "key"
    }
    nouns.append(data)

    data = {
        "ID": 21,
        "noun": "treasure"
    }
    nouns.append(data)

    data = {
        "ID": 18,
        "noun": "rimmer"
    }
    nouns.append(data)

    data = {
        "ID": 12,
        "noun": "house"
    }
    nouns.append(data)

    data = {
        "ID": 22,
        "noun": "banana"
    }
    nouns.append(data)

    data = {
        "ID": 22,
        "noun": "bananas"
    }
    nouns.append(data)

    data = {
        "ID": 23,
        "noun": "sand"
    }
    nouns.append(data)


def createVerbs(verbs):
    """
    Function createVerbs() create all verbs the game understands
    """
    # id is used for synonyms in a look-up table in functions.py. That way
    # only one match statement is needed no matter how many synonyms per
    # verb is defined
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
        "verb": "down"
    }
    verbs.append(data)
    data = {
        "ID": 17,
        "verb": "up"
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
        "verb": "break"
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

    data = {
        "ID": 9,
        "verb": "investigate"
    }
    verbs.append(data)

    data = {
        "ID": 24,
        "verb": "hint"
    }
    verbs.append(data)

    data = {
        "ID": 16,
        "verb": "d"
    }
    verbs.append(data)

    data = {
        "ID": 17,
        "verb": "u"
    }
    verbs.append(data)


def create_locations(locations):
    """
    The function create_locations() creates all the places
    the player can visited
    """

    verbose_str = "You're in limbo. Everything is as dark as one would"
    verbose_str += " expect of the afterlife.\nSorry dear, you're dead."

    data = {
        # This first location is here to make sure the map really
        # starts at 1 for game-logic purposes.
        # In "Pirate Island" this location is never used.
        # However, the code is getting flexible enough so any if-game
        # could potentially be developed using this code
        # If another game was developed using this code as the base, the player
        # could be "transported" here when they die
        # before showing the end-of-game message
        # Also used to comment what the different key:values do
        # Not repeated for other locations

        "brief": "You are in limbo.",
        # short description of location
        "verbose": verbose_str,
        # long description of location
        "outdoors": False,
        # is the location set outdoors, in case one wants certain
        # (random) events to only happen outdoors.
        "visited": False,
        # has the player been here before? Set to true whenever the player
        # enters the place. Also used to
        # determine if brief or verbose should be displayed
        "east": 0,
        # can you go in that direction? If no, set to 0. Otherwise set to the
        # location you will move to if you go in that direction. Some of these
        # values are changed during game depending on what the player do
        "west": 0,
        "south": 0,
        "north": 0,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You are at the bottom of a steep cliff. The very rock"
    verbose_str += " is as vertical as it\ncan get, and you don't fancy"
    verbose_str += " looking up since the very thought of it is"
    verbose_str += " making\nyou nauseous. There is a rope to be"
    verbose_str += " climbed back up, allowing for the vertigo."

    data = {
        "brief": "You are at the bottom of a cliff.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 0,
        "west": 0,
        "south": 5,
        "north": 0,
        "down": 0,
        "up": 2
    }
    locations.append(data)

    verbose_str = "You're at the top of a cliff. Far, far down below you can"
    verbose_str += " see a path dwindling\nsouth towards what seems to be a"
    verbose_str += " harbour. There is a huge piece of rock jutting out of"
    verbose_str += " what looks to be granite, although you can not be sure."
    verbose_str += " You \nare, after all, a pirate and not a geologist."

    data = {
        "brief": "You are the top of a cliff.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 0,
        "west": 0,
        "south": 6,
        "north": 0,
        "down": 0,
        "up": 0
    }

    locations.append(data)

    verbose_str = "You're at beach at the northern end of this rather small "
    verbose_str += "island. The ground is\nuneven and "
    verbose_str += "there are plenty of rocks of various sizes "
    verbose_str += "strewn around, making you quite happy that you are"
    verbose_str += " wearing the sturdiest boots in existance."

    data = {
        "brief": "You are at a beach.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 4,
        "west": 0,
        "south": 7,
        "north": 0,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You're at beach at the north-eastern end of this somewhat "
    verbose_str += "small island. In\nthe water you can see "
    verbose_str += "several fishes swimming by and doing whatever fishes"
    verbose_str += "\nusually do. The sand is kinda golden in look, and is "
    verbose_str += "soft to the touch."

    data = {
        "brief": "You are at a beach.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 0,
        "west": 3,
        "south": 8,
        "north": 0,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You're at the shore. It is more of a harbour really,"
    verbose_str += " with one sole\nship lying "
    verbose_str += "anchored here. The ship is "
    verbose_str += "somewhat small, but appears to be\nsea-worthy. "
    verbose_str += "A grim-looking guard watches the entry with a\nstern "
    verbose_str += "look in his eyes."

    data = {
        "brief": "You are at the shore.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 0,
        "west": 0,
        "south": 18,
        # south value is deliberately wrong.
        # Location 18 does not exist. Used for checking if guard has been
        # bribed yet
        # in go_south() function. When he is, the value will be changed to 9
        "north": 1,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You're at the edge of the jungle. Birds are chirping,"
    verbose_str += "and the "
    verbose_str += "jungle is\nnot as thick here. Which"
    verbose_str += " is good, since that means there are fewer places"
    verbose_str += "\nfor dangerous animals to hide."

    data = {
        "brief": "You are in the jungle.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 7,
        "west": 0,
        "south": 0,
        "north": 2,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You're in a clearing. In the trees surrounding the clearing"
    verbose_str += " you can see "
    verbose_str += "some\nmonkeys monkeying around. Paths lead off in all "
    verbose_str += "directions, although "
    verbose_str += "the path\nrunning to the east is blocked by a large chest."

    data = {
        "brief": "You are in a small clearing.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 0,
        "west": 6,
        "south": 11,
        "north": 3,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You're at the bottom of a hill. Sometime in the past"
    verbose_str += " someone made an artificial "
    verbose_str += "cave in it, and the entrence is to the south. However,"
    verbose_str += " the entrence is barred "
    verbose_str += "\nwith a gate."

    data = {
        "brief": "You are the bottom of a hill.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 0,
        "west": 0,
        "south": 0,
        "north": 4,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You're inside the ship. Despite its small size, it is"
    verbose_str += "clearly a very luxurous\nship and may have been "
    verbose_str += "the prized possession of some nobleman before it ended"
    verbose_str += " upat this godforsaken island. In fact, the nobleman "
    verbose_str += "is still here. He is sitting\nin a chair, although he"
    verbose_str += " could use bit more flesh on him. Mr Skeleton "
    verbose_str += "does not\nlook healthy."

    data = {
        "brief": "You are inside the ship.",
        "verbose": verbose_str,
        "outdoors": False,
        "visited": False,
        "east": 0,
        "west": 0,
        "south": 0,
        "north": 5,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You're outskirts of the jungle. Strange animal noises"
    verbose_str += "can be heard from\neverywhere, and it makes"
    verbose_str += " you feel shaky as if something wants to eat you."

    data = {
        "brief": "You are at the start of the jungle.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 11,
        "west": 0,
        "south": 14,
        "north": 0,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You're at a pathway, where paths leads in several "
    verbose_str += "directions. The air is stale."

    data = {
        "brief": "You are at pathway.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": True,
        "east": 11,
        "west": 10,
        "south": 0,
        "north": 7,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You are in a cave. It is manmade, otherwise it wouldn't be "
    verbose_str += "so perfectly square. The walls are covered in moss,"
    verbose_str += " and the floor is stone cold. Which makes sense\nsince it "
    verbose_str += "is stone. In one corner there's an old and "
    verbose_str += "unstable table standing."

    data = {
        "brief": "You are in a cave.",
        "verbose": verbose_str,
        "outdoors": False,
        "visited": False,
        "east": 0,
        "west": 0,
        "south": 0,
        "north": 8,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You are on a beach. It is like any other beach you have "
    verbose_str += "ever seen, except for\nthe large banana tree at the"
    verbose_str += " western edge. There's a wooden board nailed to the trunk."

    data = {
        "brief": "You are on a beach.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 14,
        "west": 0,
        "south": 0,
        "north": 0,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You are on a beach. It would be a lovely beach if it"
    verbose_str += " wasn't  for the fact that\nyou're marooned on this"
    verbose_str += "island. Golden sand, very clear blue"
    verbose_str += " water in the ocean, and overall"
    verbose_str += " a picturesque postcard feel to it. "
    verbose_str += "A pathway can be seen leading\ninto the jungle.\n"
    verbose_str += "\nOut at sea, you can "
    verbose_str += "see \"The Sea Monkey\" slowly sinking beneath the waves."

    data = {
        "brief": "You are on a beach.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 15,
        "west": 13,
        "south": 0,
        "north": 10,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You are on the eastern end of the beach. It still"
    verbose_str += " looks lovely, but that\nold and"
    verbose_str += " worn-out house ruins the look. The door is closed."

    data = {
        "brief": "You are on a beach.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 0,
        "west": 14,
        "south": 0,
        "north": 0,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You are inside the building. The question that occurs: "
    verbose_str += "why bother locking it? \nIt is completely"
    verbose_str += " devoid of furniture or interesting features."

    data = {
        "brief": "You are inside the building.",
        "verbose": verbose_str,
        "outdoors": False,
        "visited": False,
        "east": 0,
        "west": 15,
        "south": 0,
        "north": 0,
        "down": 0,
        "up": 0
    }
    locations.append(data)

    verbose_str = "You are in another clearing. Someone has used some "
    verbose_str += "vines to create\nan X on the ground."

    data = {
        "brief": "You are in another clearing.",
        "verbose": verbose_str,
        "outdoors": True,
        "visited": False,
        "east": 4,
        "west": 0,
        "south": 0,
        "north": 0,
        "down": 0,
        "up": 0
    }
    locations.append(data)
