opening_text = """You awaken in a room, it is dim but you can make out a door on each wall. There are no windows.
The door to the north seems to be the main door, there is a padlock keeping it locked shut.
You are on the bed, it is perfectly made apart from where you've moved it as you sat up.
"""

kitchen_description = """Kitchen
"""

bathroom_description = """Bathroom
"""

cupboard_description = """Cupboard
"""

help_guide = """Basic commands: 
'north', 'south', 'east', 'west' to move around the room. 
use [item] to use something.
examine [object] to get a closer look."""


def kitchen_scene():  # defining the kitchen scene
    print(kitchen_description)
    exit()


def bathroom_scene():  # defining the bathroom scene
    print(bathroom_description)
    exit()


def cupboard_scene():  # defining the cupboard scene
    print(cupboard_description)
    exit()


print(opening_text)  # prints out the opening text which is defined earlier
directions = ["north", "east", "south", "west"]
starting_room_options = input("").lower()  # submit directions, and change anything entered to lowercase
while starting_room_options in directions:  # if directions not entered will repeat until direction is given

    if starting_room_options == "south":  # if south is entered will carry out these functions:
        kitchen_scene()

    elif starting_room_options == "west":  # if west is entered will carry out these functions:
        bathroom_scene()

    elif starting_room_options == "east":  # if south is entered will carry out these functions:
        cupboard_scene()
else:
    print("I do not understand")  # asking the player to reenter

