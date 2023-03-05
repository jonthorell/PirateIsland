# This file creates all lists/dics necessary for the game

def createObjects(objects):
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
    "location": -1,
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
    "gettable": False,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 2,
    "noun": "bottle",
    "description": "a dirty old bottle",
    "exam": "The bottle might have contained rum at one point. There seems to be something else inside it now, a piece of paper.",
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
    
    data = {
    "ID": 4,
    "noun": "map",
    "description": "a treasure map",
    "exam": "The paper the map is written on seems to be fragile. Probably due to having been subjected to some liquid before.",
    "location": 4,
    "gettable": True,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 5,
    "noun": "skeleton",
    "description": "Mr skeleton",
    "exam": "The skeleton is wearing what was once very nice clothes. Now the clothes looks nothing like clothes, more like holes with remnants of fabric around it.",
    "location": 9,
    "gettable": False,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 6,
    "noun": "paper",
    "description": "a piece of paper",
    "exam": "The piece of paper is partially crumbled, but there are some words written on it.",
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
    
    data = {
    "ID": 8,
    "noun": "rope",
    "description": "a long rope",
    "exam": "A long rope made of the finest Hithlain. Elven-made when elves still roamed middle-earth.",
    "location": 12,
    "gettable": True,
    "visible": True
}
    objects.append(data)
    
    data = {
    "ID": 9,
    "noun": "table",
    "description": "an unstable table",
    "exam": 'The table is made of balsa wood. No wonder it is unstable. Someone has carved "Smeagol was here" in it.',
    "location": 12,
    "gettable": False,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 10,
    "noun": "ring",
    "description": "a golden ring",
    "exam": "The ring is perfectly cirular with a huge diamond decorating it.",
    "location": 3,
    "gettable": True,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 11,
    "noun": "board",
    "description": "a wooden board",
    "exam": "What do you expect? It is a wooden board. However, there's some writing on it.",
    "location": 13,
    "gettable": False,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 12,
    "noun": "building",
    "description": "a building",
    "exam": "The building seems to have been built using whatever could be salvaged from various shipwrecks. Good craftsman skills of whoever built it though since it looks like it could withstand anything.",
    "location": 15,
    "gettable": False,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 13,
    "noun": "door",
    "description": "a door",
    "exam": "The door is made out of metal, and there's a small keyhole in it.",
    "location": 15,
    "gettable": False,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 14,
    "noun": "shovel",
    "description": "a small shovel",
    "exam": "Just your ordinary treasure-hunting shovel. A must have for any respectable pirate.",
    "location": 16,
    "gettable": True,
    "visible": True
}
    objects.append(data)
    
    data = {
    "ID": 15,
    "noun": "ship",
    "description": "a pirate vessel",
    "exam": "The pirate vessel, \"The Sea Monkey\" is too far out of your reach to be examined. You know it inside-out anyway.",
    "location": 14,
    "gettable": False,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 16,
    "noun": "banana-tree",
    "description": "a banana-tree",
    "exam": "The banana-tree is full of overripe bananas. They look disgusting.",
    "location": 13,
    "gettable": False,
    "visible": False
}
    objects.append(data)
    
    data = {
    "ID": 17,
    "noun": "rocks",
    "description": "a bunch of rocks",
    "exam": "When you examine the rocks, you discover a golden ring amongst them.",
    "location": 5,
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
    
    data = {
    "ID": 20,
    "noun": "key",
    "description": "a small key",
    "exam": "The key seems to be made out of silver and some other unknown ore.",
    "location": 7,
    "gettable": True,
    "visible": False
}
    objects.append(data)
    
def createNouns(nouns):
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
    

def createVerbs (verbs):
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
    
def create_locations (locations):
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
    "north": 0,
    "down": 0,
    "up": 0
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
    "north": 0,
    "down": 0,
    "up": 2    
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
    "north": 0,
    "down": 0,
    "up": 0
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
    "north": 0,
    "down": 0,
    "up": 0
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
    "north": 0,
    "down": 0,
    "up": 0
}
    locations.append(data)
    
    data = {
    "brief": "You are at the shore.",
    "verbose": "You're at the shore. It is more of a harbour really, with one sole ship lying anchored here. The ship is somewhat small, but appears to be sea-worthy. A grim-looking guard watches the entry with a stern look in his eyes.",
    "outdoors": True,
    "visited": False,
    "east": 0,
    "west": 0,
    "south": 9,
    "north": 1,
    "down": 0,
    "up": 0
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
    "north": 2,
    "down": 0,
    "up": 0
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
    "north": 3,
    "down": 0,
    "up": 0
}
    locations.append(data)

    data = {
    "brief": "You are the bottom of a hill.",
    "verbose": "You're at the bottom of a hill. Sometime in the past someone made an artificial cave in it, and the entrence is to the south. However, the entrence is barred with a gate.",
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
    
    data = {
    "brief": "You are inside the ship.",
    "verbose": "You're inside the ship. Despite its small size, it is clearly a very luxurous ship and may have been the prized possession of some nobleman before it ended up at this godforsaken island. In fact, the nobleman is still here. He is sitting in a chair, although he could use bit more flesh on him. Mr Skeleton does not look healthy.",
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
    
    data = {
    "brief": "You are at the start of the jungle.",
    "verbose": "You're outskirts of the jungle. Strange animal noises can be heard from everywhere, and it makes you feel shaky as if something wants to eat you.",
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
    
    data = {
    "brief": "You are at pathway.",
    "verbose": "You're at a pathway, where paths leads in several directions. The air is stale.",
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
    
    data = {
    "brief": "You are in a cave.",
    "verbose": "You are in a cave. It is manmade, otherwise it wouldn't be so perfectly square. The walls are covered in moss, and the floor is stone cold. Which makes sense since it is stone. In one corner there's an old and unstable table standing.",
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
    
    data = {
    "brief": "You are on a beach.",
    "verbose": "You are on a beach. It is like any other beach you have ever seen, except for the large banana tree at the western edge. There's a wooden board nailed to the trunk.",
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
    
    data = {
    "brief": "You are on a beach.",
    "verbose": "You are on a beach. It would be a lovely beach if it wasn't for the fact that you're marooned on this island. Golden sand, very clear blue water in the ocean, and overall a picturesque postcard feel to it. A pathway can be seen leading into the jungle.\nOut at sea, you can see \"The Sea Monkey\" slowly sinking beneath the waves.",
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
    
    data = {
    "brief": "You are on a beach.",
    "verbose": "You are on the eastern end of the beach. It still looks lovely, but that old and worn-out house ruins the look. The door is closed.",
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
    
    data = {
    "brief": "You are inside the building.",
    "verbose": "You are inside the building. The question that occurs: why bother locking it? It is completely devoid of furniture or interesting features.",
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
    
    data = {
    "brief": "You are in another clearing.",
    "verbose": "You are in another clearing. Someone has used some vines to create an X on the ground.",
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

