import os

inventory = []  # inventory list
box = False  # sets the box as closed

# opening descriptions
opening_text = """You awaken in a room that you do not recognise with no memories on how you got here, you remember most
of yesterday but after leaving work in the evening it all goes blank. You should probably get out of here, your cat will
be hungry if you don't get home soon. When you think about it you're not sure what time it is nor how long you've been
asleep.  
"""

# different room descriptions
starting_room_description = """The room is dim but you can make out a door on each wall. There are no windows.
The door to the north seems to be the main door, there is a padlock keeping it locked shut. You are on the bed, 
it is perfectly made apart from where you've moved it as you got up. There are two beside tables, one contains a lamp
both have draws that are currently shut."""

kitchen_description = """The room you enter is a kitchen, the oven and fridge are old and run down. You can tell from 
here they barely work. The cupboards are stocked well enough from what you can see, generic store brand version of all 
the items. In the corner of the room theres a table, two chairs due to the small size of the room and a box sits in the 
middle. Above the table there is a small window right at the top of the wall, you could not fit through it and would
need to stand on a chair in order to see through it.
"""

bathroom_description = """The room is barely big enough for two people and contains a shower, toilet and sink sit within
the room. In the top right corner on the wall with the door there is vent. On the sink there is pot with four 
toothbrushes. They seem to be brand new. The mat on the floor also looks to be brand new. 
"""

cupboard_description = """The room turns out to not be a room but is in fact a cupboard. There is a string attached to 
the light but when you pull it it fails to turn on. You cannot tell what is on the shelves in this light but they seem
to be stocked well. There are multiple boxes in the corner on the floor. 
"""

# basic help guide of commands that can be written
help_guide = """\033[1;31m
- Basic commands: 
- 'north', 'south', 'east', 'west' to move around the room. 
- use [item] to use something.
- examine [object] to get a closer look.
- inventory to open your inventory.\n \033[0;39m \n"""  #/033[0;31m and /n make the text appear red then \033[0;39m \n turns it back to white


# the point in scenes the player will go back to when an action is completed in order to stop them from having to read the descriptions each time
def starting_room_scene_restart():  # defining the point in which players return to after completing an action

    print("")
    starting_room_options = input("What would you like to do? ").lower()  # submit directions, and change anything entered to lowercase
    if starting_room_options == "south":  # if south is entered will carry out these functions:
        kitchen_scene()  # starts the kitchen scene

    elif starting_room_options == "west":  # if west is entered will carry out these functions:
        bathroom_scene()  # starts the bathroom scene

    elif starting_room_options == "east":  # if south is entered will carry out these functions:
        cupboard_scene()  # starts the cupboard scene

    elif starting_room_options == "north":  # if north is entered will carry out these functions:
        print("The door is padlocked shut, you pull at the handle and it doesn't move.")
        starting_room_scene_restart()

    elif starting_room_options == "help":  # if help is entered will carry out these functions:
        print(help_guide)  # displays the help guide
        starting_room_scene_restart()  # goes back to the beginning of the scene

    elif starting_room_options == "inventory":  # if inventory is entered will carry out these functions:
        print(inventory)  # displays the inventory guide
        starting_room_scene_restart()  # goes back to the beginning of the scene
    else:
        print("I do not understand, type help for general instructions.")  # asking the player to reenter
        starting_room_scene_restart()


def kitchen_scene_restart():  # defining the point in which players return to after completing an action
    global box  # declares the global box variable within this scene
    print("")
    kitchen_options = input("What would you like to do? ").lower()
    if kitchen_options == "north":  # if north is entered will carry out these functions:
        starting_room_scene()  # will return the player to the starting room

    elif box == False and kitchen_options == "examine box":  # checks if the box has been opened + what the player typed
        box_pickup = input("""The box is just big enough to hold a handful of golf balls, the design is very detailed 
but a little ugly. Would you like to open the box? """).lower()

        if box_pickup == "yes":
            print("""You reach into the box and there sits a rusted, falling apart screwdriver. It's kind of a weird 
place to keep it, instead of thinking to hard about the really strange place to keep a tool you shove it into your 
pocket for later use.""")
            inventory.append("Rusted Screwdriver")
            box = True  # whether or not the box has been interacted with, switches back when code restarts
            kitchen_scene_restart()

        elif box_pickup == "no":
            print("The box remains shut on the table and the contains remain unknown.")
            kitchen_scene_restart()

        else:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter
            kitchen_scene_restart()

    elif box == True and kitchen_options == "examine box":  # checks if the box has been opened + what the player typed
        print("The box remains open on the table, it is empty.")
        kitchen_scene_restart()

    elif kitchen_options == "examine fridge":  # if examine fridge is entered will carry out these functions:
        print("Unlike the cupboards the fridge is not well stocked, there is a few bottles of water but that is it.")
        kitchen_scene_restart()

    elif kitchen_options == "examine chair":  # if examine chair is entered will carry out these functions:
        print("""The chair is nothing special but if you stood on the chair you would be able to see out the little 
window, it seems practically new.""")
        kitchen_scene_restart()

    elif kitchen_options == "stand on chair":  # if stand on chair is entered will carry out these functions:
        print("""You climb onto the chair, it rocks gently beneath you but you hold out your arms to balance yourself.
Once you are up there you can't see anything new in the room but you are able to see out the little window. From what
you can tell you must be in a basement since you can only see the bottom of trees from your postion.""")
        kitchen_scene_restart()

    elif kitchen_options == "help":  # if help is entered will carry out these functions:
        print(help_guide)
        kitchen_scene_restart()

    elif kitchen_options == "inventory":  # if inventory is entered will carry out these functions:
        print(inventory)  # displays the inventory guide
        kitchen_scene_restart()  # goes back to the beginning of the scence

    else:
        print("I do not understand, type help for general instructions.")  # asking the player to reenter
        kitchen_scene_restart()


def bathroom_scene_restart():  # defining the point in which players return to after completeing an action
    print("")
    bathroom_options = input("What would you like to do? ").lower()
    if bathroom_options == "east":  # if east is entered will carry out these functions:
        starting_room_scene()  # will return the player to the starting room


def cupboard_scene_restart():  # defining the point in which players return to after completeing an action
    print("")
    cupboard_options = input("What would you like to do? ").lower()
    if cupboard_options == "west":  # if west is entered will carry out these functions:
        starting_room_scene()  # will return the player to the starting room



# all scenes that include the descriptions of the room


def cupboard_scene():  # defining the cupboard scene
    print(cupboard_description)  # displays the cupboard description
    print("")
    cupboard_scene_restart()   # starts the cupboard scene from a point that doesn't include the room descriptions


def starting_room_scene():  # defining the starting room scene
    print(starting_room_description)  # displays the starting room description
    print("")
    starting_room_scene_restart()   # starts the starting scene from a point that doesn't include the room descriptions


def bathroom_scene():  # defining the bathroom scene
    print(bathroom_description)  # displays the bathroom description
    print("")
    bathroom_scene_restart()   # starts the bathroom scene from a point that doesn't include the room descriptions


def kitchen_scene():  # defining the kitchen scene
    print(kitchen_description)  # displays the kitchen description
    print("")
    kitchen_scene_restart()   # starts the kitchen scene from a point that doesn't include the room descriptions


print(opening_text)  # displays the opening text which is defined earlier
starting_room_scene()  # starts the starting scene