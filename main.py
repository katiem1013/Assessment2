# opening descriptions
opening_text = """You awaken in a room, it is dim but you can make out a door on each wall. There are no windows.
The door to the north seems to be the main door, there is a padlock keeping it locked shut.
You are on the bed, it is perfectly made apart from where you've moved it as you sat up.
"""

# different room descriptions
kitchen_description = """The room you enter is a kitchen, the oven and fridge are old and run down. You can tell from 
here they barely work. The cupboards are stocked well enough from what you can see, generic store brand version of all 
the items. In the corner of the room theres a table, two chairs due to the small size of the room and a box sits in the 
middle.
"""

bathroom_description = """The room is barely big enough for two people and contains a shower, toilet and sink sit within
the room. In the top right corner on the wall with the door there is vent. On the sink there is pot with four 
toothbrushes. They seem to be brand new. The mat on the floor also looks to be brand new. 
"""

cupboard_description = """The room turns out to not be a room but is in fact a cupboard. There is a string attached to 
the light but when you pull it it fails to turn on. You cannot tell what is on the shelves in this light but they seem
to be stocked well. There are multiple boxes in the corner on the floor. 
"""

# basic commands that can be written
help_guide = """Basic commands: 
'north', 'south', 'east', 'west' to move around the room. 
use [item] to use something.
examine [object] to get a closer look."""


def kitchen_scene():  # defining the kitchen scene
    print(kitchen_description)
    input("What would you like to do? ")


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

