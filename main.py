opening_text = """You awaken in a room, it is dim but you can make out a door on each wall. There are no windows.
The door to the north seems to be the main door, there is a padlock keeping it locked shut.
You are on the bed, it is perfectly made apart from where you've moved it as you sat up.
"""

help_guide = """Basic commands: 
'north', 'south', 'east', 'west' to move around the room. 
use [item] to use something.
examine [object] to get a closer look."""

print(opening_text)
directions = ["north", "east", "south", "west"]
starting_room_options = input("").lower()  # submit directions, and change anything entered to lowercase
if starting_room_options in directions:  # if directions not entered will repeat until direction is given

    if starting_room_options == "south":  # if south is entered will carry out these functions:
        print("hello")
else:
    print("I do not understand")  # asking the player to reenter
    exit()