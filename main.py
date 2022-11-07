opening_text: """ """

print(opening_text)

print("You have awoken in a forest, there are four ways you can go. ")
input("")
directions = ["north", "east", "south", "west"]
while directions is not int:  # if directions not entered will repeat until direction is given
    print("options are 'north' 'east' 'south' 'west' ")  # example of directions
    input("")  # resubmit directions

    if int == "south":  # if south is entered will carry out these functions:
        cabin_scene()  # calling the cabin function


def cabin_scene():
    print("You come across an abandoned cabin.")
