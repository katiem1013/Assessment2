directions = ["north", "east", "south", "west", "help"]
inventory = []

# opening descriptions
opening_text = """You awaken in a room that you do not recognise with no memories on how you got here 
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
help_guide = """\033[0;31m
- Basic commands: 
- 'north', 'south', 'east', 'west' to move around the room. 
- use [item] to use something.
- examine [object] to get a closer look.
- inventory to open your inventory.\n \033[0;39m \n"""  #/033[0;31m and /n make the text appear red then \033[0;39m \n turns it back to white


def kitchen_scene():  # defining the kitchen scene
    print(kitchen_description)
    def kitchen_scene_restart():  # defining the point in which players return to after completeing an action
        kitchen_options = input("What would you like to do? ").lower()
        if kitchen_options == "north":  # if south is entered will carry out these functions:
            starting_room_scene()  # will return the player to the starting room

        elif kitchen_options == "west":  # if west is entered will carry out these functions:
            bathroom_scene()

        elif kitchen_options == "east":  # if south is entered will carry out these functions:
            cupboard_scene()

        elif kitchen_optionsstarting_room_options == "help":  # if help is entered will carry out these functions:
            print(help_guide)
            kitchen_scene_restart()
        else:
            print("I do not understand")  # asking the player to reenter
            kitchen_scene_restart()

def bathroom_scene():  # defining the bathroom scene
    print(bathroom_description)
    exit()


def cupboard_scene():  # defining the cupboard scene
    print(cupboard_description)
    exit()


def starting_room_scene():  # defining the starting room scene
    print(starting_room_description)  # displays the starting room description
    def starting_room_scene_restart():  # defining the point in which players return to after completeing an action
        starting_room_options = input("What would you like to do? ").lower()  # submit directions, and change anything entered to lowercase
        while starting_room_options in directions:  # if directions not entered will repeat until direction is given

            if starting_room_options == "south":  # if south is entered will carry out these functions:
                kitchen_scene()

            elif starting_room_options == "west":  # if west is entered will carry out these functions:
                bathroom_scene()

            elif starting_room_options == "east":  # if south is entered will carry out these functions:
                cupboard_scene()

            elif starting_room_options == "help":  # if help is entered will carry out these functions:
                print(help_guide)
                starting_room_scene_restart()
        else:
            print("I do not understand")  # asking the player to reenter
            starting_room_scene_restart()

print(opening_text)  # displays the opening text which is defined earlier
starting_room_scene()
