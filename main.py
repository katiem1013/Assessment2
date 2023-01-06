import random

inventory = []  # inventory list

# variables for inside the house
box = False  # sets the box in the kitchen as closed
bedside_draw = False  # sets the bedside table in the starting room draws as closed
safe_code = []  # list for the safe code in the bathroom once it has been randomly chosen
codes_cracked = 0  # the amount of successful attempts there have been to open the bathroom safe
safe_opened = False  # sets the bathroom safe as closed
vent_opened = False  # sets the bathroom vent as closed
stool_in_bathroom = False  # sets the stool in the bathroom as no
flashlight_with_batteries = False  # sets the flashlight with batteries as no

# opening descriptions
opening_text = """You awaken in a room that you do not recognise with no memories on how you got here, you remember most
of yesterday but after leaving work in the evening it all goes blank. You should probably get out of here, your cat will
be hungry if you don't get home soon. When you think about it you're not sure what time it is nor how long you've been
asleep.  
"""

# different room descriptions
starting_room_description = """The room is dim but you can make out a door on each wall. There are no windows.
The door to the north seems to be the main door, there is a padlock keeping it locked shut. You are on the bed, 
it is perfectly made apart from where you've moved it as you got up. There are two bedside tables, one contains a lamp
both have draws that are currently shut."""

kitchen_description = """The room you enter is a kitchen, the oven and fridge are old and run down. You can tell from 
here they barely work. The cupboards are stocked well enough from what you can see, generic store brand version of all 
the items. In the corner of the room theres a table, one chair due to the small size of the room and a box sits in the 
middle. Above the table there is a small window right at the top of the wall, you could not fit through it and would
need to stand on a chair in order to see through it.
"""

bathroom_description = """The room is barely big enough for two people and contains a shower, toilet and sink sit within
the room. In the top right corner on the wall with the door there is vent. On the sink there is pot with four 
toothbrushes. They seem to be brand new. The mat on the floor also looks to be brand new. 
"""

cupboard_description = """The room turns out to not be a room but is in fact a cupboard. There is a string attached to 
the light but when you pull it it fails to turn on. You cannot tell what is on the shelves in this light but they seem
to be stocked well. There are multiple boxes in the corner on the floor with a stool tucked behind them. 
"""

# basic help guide of commands that can be written
# /033[0;31m and /n make the text appear red
help_guide = """\033[1;31m
- Basic commands: 
- 'north', 'south', 'east', 'west' to move around the room. 
- use [item] to use something.
- examine [object] to get a closer look.
- inventory to open your inventory.\n \033[0;39m \n"""  # \033[0;39m \n turns it back to white


# the point in scenes the player will go back to when an action is completed
# in order to stop them from having to read the descriptions each time
def starting_room_scene_restart():  # defining the point in which players return to after completing an action

    global bedside_draw  # declares the global bedside_draw variable within this scene
    global flashlight_with_batteries  # declares the global flashlight with batteries variable within this scene
    starting_room_options = input("What would you like to do? ").lower()  # gets the players input
    # . lower() changes anything entered to lowercase

    if starting_room_options == "south":  # if south is entered it will carry out these functions:
        kitchen_scene()  # starts the kitchen scene

    elif starting_room_options == "west":  # if west is entered it will carry out these functions:
        bathroom_scene()  # starts the bathroom scene

    elif starting_room_options == "east":  # if south is entered it will carry out these functions:
        cupboard_scene()  # starts the cupboard scene

    elif starting_room_options == "north":  # if north is entered it will carry out these functions:
        print("The door is padlocked shut, you pull at the handle and it doesn't move.")  # displays the description
        starting_room_scene_restart()  # goes back to the beginning of the scene

    elif starting_room_options == "examine bed":  # if bed is entered it will carry out these functions:
        print("""Other then where you were sleeping the bed is made perfectly, you crouch down and under the bed it is
empty, it looks as though something was once there but whatever it was is gone. It's dusty, the dirtiest thing you've 
seen so far. Whatever was there was dragged out recently.""")  # displays the description
        starting_room_scene_restart()  # goes back to the beginning of the scene

    # if examine bedside table(s) is entered it will carry out these functions:
    elif starting_room_options == "examine bedside table" or starting_room_options == "examine bedside tables":
        print("""Both bedside tables, like everything in the room, look new. One contains a lamp, it doesn't work when 
you pull it. There is one draw in both beside tables""")  # displays the description
        starting_room_scene_restart()  # goes back to the beginning of the scene

    elif starting_room_options == "examine lamp":  # if examine lamp is entered it will carry out these functions:
        print("""Upon closer inspection on the lamp you realise that where you though it was a normal lamp it is in fact
a horse. A horse with a lampshade on its head, you aren't sure where the on switch is and are kind of scared to find
out. It's actually pretty cool, you consider buying one but as you're inspecting it you see the price tag. £5,509. You 
put it back down, maybe not then.""")  # displays the description
        starting_room_scene_restart()  # goes back to the beginning of the scene

    elif starting_room_options == "examine padlock":  # if examine padlock is entered it will carry out these functions:
        print("""The padlock needs key to unlock it, out of everything you've seen so far it's the most well used. It 
has scratches covering it as though someones been yanking it, or at the very least has had it attached to something that
bashed it about a lot.""")  # displays the description
        starting_room_scene_restart()  # goes back to the beginning of the scene

    # if the beside draws have yet to be opened it will carry out these functions:
    elif (starting_room_options == "use draws" or starting_room_options == "open draws") and bedside_draw is False:
        print("""When you check both draws one contains two batteries, the other empty. You shove the batteries into
    your pocket and shut the draws.""")  # displays the description
        inventory.append("batteries")  # adds batteries to the inventory
        bedside_draw = True  # sets the beside draws as open

        # if the flashlight and batteries are in the inventory it will carry out these functions:
        if (inventory == "flashlight" and "batteries") and flashlight_with_batteries is False:
            print("You take a moment to put the batteries in the flashlight.")  # displays the description
            inventory.remove("batteries")  # removes batteries from inventory
            flashlight_with_batteries = True  # sets the flashlight with batteries variable as true
            starting_room_scene_restart()  # goes back to the beginning of the scene

        else:  # if no other option is fitting it will carry out these functions:
            starting_room_scene_restart()  # goes back to the beginning of the scene

    # beside draw function but non-plural
    elif (starting_room_options == "use draw" or starting_room_options == "open draw") and bedside_draw is False:
        print("""When you check both draws one contains two batteries, the other empty. You shove the batteries into
your pocket and shut the draws.""")  # displays the description
        inventory.append("batteries")  # adds batteries to the inventory
        bedside_draw = True  # sets the beside draws as open

        # if the flashlight and batteries are in the inventory it will carry out these functions:
        if (inventory == "flashlight" and "batteries") and flashlight_with_batteries is False:
            print("You take a moment to put the batteries in the flashlight.")  # displays the description
            inventory.remove("batteries")  # removes batteries from inventory
            flashlight_with_batteries = True  # sets the flashlight with batteries variable as true
            starting_room_scene_restart()  # goes back to the beginning of the scene

        else:  # if no other option is fitting it will carry out these functions:
            starting_room_scene_restart()  # goes back to the beginning of the scene

    # if the beside draw has been opened it will carry out these functions:
    elif (starting_room_options == "use draw" or starting_room_options == "open draw") and bedside_draw is True:
        print("When you open the draws they are both empty.")  # displays the description
        starting_room_scene_restart()  # goes back to the beginning of the scene

    elif starting_room_options == "use key" and "key" in inventory:
        print("yay!")

    elif starting_room_options == "help":  # if help is entered it will carry out these functions:
        print(help_guide)  # displays the help guide
        starting_room_scene_restart()  # goes back to the beginning of the scene

    elif starting_room_options == "inventory":  # if inventory is entered it will carry out these functions:
        print(inventory)  # displays the inventory guide
        starting_room_scene_restart()  # goes back to the beginning of the scene

    else:  # if no other option is fitting it will carry out these functions::
        print("I do not understand, type help for general instructions.")  # asking the player to reenter
        starting_room_scene_restart()  # goes back to the beginning of the scene


def kitchen_scene_restart():  # defining the point in which players return to after completing an action
    global box  # declares the global box variable within this scene
    kitchen_options = input("What would you like to do? ").lower()  # gets the players input
    if kitchen_options == "north":  # if north is entered will carry out these functions:
        starting_room_scene()  # will return the player to the starting room

    elif box is False and kitchen_options == "examine box":  # checks if the box has been opened + what the player typed
        print("""The box is just big enough to hold a handful of golf balls, the design is very detailed 
but a little ugly.""")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif box is True and kitchen_options == "examine box":  # checks if the box has been opened + what the player typed
        print("The box remains open on the table, it is empty.")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif kitchen_options == "examine fridge":  # if examine fridge is entered it will carry out these functions:
        print("""Unlike the cupboards the fridge is not well stocked, there is a few bottles of water on one of the 
shelves. The first one you pick up has been opened and is missing some water. The rest have not been. When the water is 
in your hand you notice that it is far too warm for being in the fridge.""")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif kitchen_options == "examine chair":  # if examine chair is entered it will carry out these functions:
        print("""The chair is nothing special but if you stood on the chair you would be able to see out the little 
window, it seems practically new.""")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif kitchen_options == "examine window":  # if examine window is entered it will carry out these functions:
        print("""You are unable to see out of the window from here, when you stand back you are able to see the sky but
you can't quite tell what time it is.""")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif kitchen_options == "examine table":  # if examine table is entered it will carry out these functions:
        print("""The table looks somewhat new, there are scratches on the edge you can't tell what made them. There is 
a box sitting in the middle if not a little closer to the left side. The table is made of wood unlike the chair tucked
under it which is made out of metal.""")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif kitchen_options == "examine oven":  # if examine oven is entered it will carry out these functions:
        print("""From what you can tell the oven is gas, you reach out and try to turn it on but nothing you do works.
When you try to pull open the main oven it won't move no matter how hard you pull it.""")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif kitchen_options == "examine cupboards":  # if examine cupboards is entered it will carry out these functions:
        print("""Upon further inspection while the cupboards appear to be well stocked everything has been pulled to the
front edge of them. You pick up the closest can and realise it's empty. You replace it in the cupboard and pick up 
another, it's also empty.""")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif kitchen_options == "examine cupboard":  # if examine cupboard is entered it will carry out these functions:
        print("""Upon further inspection while the cupboards appear to be well stocked everything has been pulled to the
front edge of them. You pick up the closest can and realise it's empty. You replace it in the cupboard and pick up 
another, it's also empty.""")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    # if stand on chair or use chair is entered it will carry out these functions:
    elif kitchen_options == "stand on chair" or kitchen_options == "use chair":
        print("""You climb onto the chair, it rocks gently beneath you and creaks loudly in the silent room but you hold
out your arms to balance yourself. bOnce you are up there you can't see anything new in the room but you are able to see
out the little window. From what you can tell you must be in a basement since you can only see the bottom of trees from 
your position. Even from up here you cant quite tell what time it is.""")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    # if open box or use box is entered and the box hasn't been opened it will carry out these functions:
    elif (kitchen_options == "use box" or kitchen_options == "open box") and box is False:
        print("""You reach into the box and there sits a rusted, falling apart screwdriver. It's kind of a weird 
place to keep it, instead of thinking to hard about the really strange place to keep a tool you shove it into your 
pocket for later use.""")  # displays the description
        inventory.append("screwdriver")  # adds the screwdriver to the inventory
        box = True  # sets the box to true to confirm it's been opened
        kitchen_scene_restart()  # goes back to the beginning of the scene

    # if open box or use box is entered and the box has been opened it will carry out these functions:
    elif (kitchen_options == "use box" or kitchen_options == "open box") and box is True:
        print("The box is empty, you already took the screwdriver from it.")  # displays the description
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif kitchen_options == "help":  # if help is entered it will carry out these functions:
        print(help_guide)
        kitchen_scene_restart()  # goes back to the beginning of the scene

    elif kitchen_options == "inventory":  # if inventory is entered it will carry out these functions:
        print(inventory)  # displays the inventory guide
        kitchen_scene_restart()  # goes back to the beginning of the scene

    else:  # if no other option is fitting it will carry out these functions:
        print("I do not understand, type help for general instructions.")  # asking the player to reenter
        kitchen_scene_restart()


def bathroom_scene_restart():  # defining the point in which players return to after completing an action

    global safe_opened  # declares the global safe opened variable within this scene
    global stool_in_bathroom   # declares the global stool in bathroom variable within this scene

    bathroom_options = input("What would you like to do? ").lower()  # gets the players input
    if bathroom_options == "east":  # if east is entered it will carry out these functions:
        starting_room_scene()  # will return the player to the starting room

    elif bathroom_options == "examine shower":  # if examine shower is entered it will carry out these functions:
        print("""It's one of those showers that is shoved into the corner of the room and would usually have two glass 
doors that open on the corner but instead it is two shower curtains, when you push them back there are a range of shower
products. A weird amount really.""")  # displays the description
        bathroom_scene_restart()  # goes back to the beginning of the scene

    elif bathroom_options == "examine toilet":  # if examine toilet is entered it will carry out these functions:
        print("""Upon closer inspection you think, wow, that sure is a toilet. It might possibly be the most average 
toilet you've ever seen.""")  # displays the description
        bathroom_scene_restart()  # goes back to the beginning of the scene

    elif bathroom_options == "examine sink":  # if examine sink is entered it will carry out these functions:
        print("""If a sink could appear in the dictionary next to the word sink there is a real chance it could be this 
one. It is a picture perfect sink.""")  # displays the description
        bathroom_scene_restart()  # goes back to the beginning of the scene

    elif bathroom_options == "examine vent":  # if examine vent is entered it will carry out these functions:
        print("The vent is pretty high up, you can't quite reach it from here.")  # displays the description
        bathroom_scene_restart()  # goes back to the beginning of the scene

    elif bathroom_options == "examine toothbrushes":  # if examine padlock is entered it will carry out these functions:
        print("""Three toothbrushes sit in a pot, they're the only things in there. There's a green, blue and purple one 
The green has obviously been use, though it's unclear how recently.""")  # displays the description
        bathroom_scene_restart()  # goes back to the beginning of the scene

    elif bathroom_options == "examine mat":  # if examine padlock is entered it will carry out these functions:
        print("""While it's obviously supposed to be white you can tell even from the door that it's greying from use. 
It's bone dry, well dead bone dry, alive bones are actually wet. You don't really think much of the mat though it looks 
as though there is something underneath.""")  # displays the description
        bathroom_scene_restart()  # goes back to the beginning of the scene

    # if examine use mat or move mat is entered will carry out these functions:
    elif bathroom_options == "use mat" or bathroom_options == "move mat":
        print("""When you move the mat theres a safe underneath, you aren't sure what the code is but theres tree notes 
on the bottom of the mat it read:""")  # displays the description

        if safe_opened is False:  # if safe has not been opened carry out these functions:
            global safe_code  # declares the global safe code variable within this scene
            while len(safe_code) < 1:  # checks how many successful attempt there have already been
                code = random.randint(3, 12)  # randomises what numbers the is, between 3 and 12
                if code not in safe_code:  # checks to see if the number has already been chosen
                    safe_code.append(code)  # adds the number to the code list if they haven't already been used
                global codes_cracked  # declares the global code cracked variable within this scene

                # while the number of successful attempts is less than three the code will repeat
                while codes_cracked < len(safe_code):
                    print("you must enter a pair of numbers that divide to %d." % code)  # tells the player what to do
                    try:  # catches errors, instead of stopping the code it reruns
                        player_number_1 = float(input("Enter number: "))  # asking the player to enter a number
                        player_number_2 = float(input("Enter number: "))  # asking the player to enter a number
                        result = player_number_1 // player_number_2  # divides the numbers given
                        if result == code:  # if the result is the same as the code these functions will happen:
                            print("Correct.")  # confirms the guess was correct
                            codes_cracked += 1  # adds 1 to the amount of successful attempts

                    except ValueError:  # if the player enters anything but a number these functions will happen:
                        print("Not a number.")  # confirms it is not a number
                        break  # stops the loop and skip to the next code after the loo

                    except ZeroDivisionError:  # if the player enters 0 these functions will happen:
                        print("Can't divide by zero.")  # confirms they cannot divide by 0

                else:
                    print("You have opened the safe.")  # displays the description
                    print("""You think it's kind of weird that whoever lives here put the code to the safe on the mat 
hiding it, and even weirder they did it as a riddle, but it works out for you because it clicks open and you are able to 
reach in and pull out a... you can't actually tell what it is. It's paper, green, kind of crushed. It might be a frog? 
Judging by the eyes and weird uneven legs. A solid attempt, just not a great one. The state of it makes you feel less
guilty when you unfold it and find a singular word written on it: Fireplace... 
What does that mean?
""")  # displays the description
                    bathroom_scene_restart()  # goes back to the beginning of the scene

        elif safe_opened is True:  # of safe has been opened carry out these functions:
            print("The safe is unlocked but close. It remains empty.")
            bathroom_scene_restart()  # goes back to the beginning of the scene

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter
            bathroom_scene_restart()  # goes back to the beginning of the scene

    elif "stool" in inventory and (bathroom_options == "use stool" or bathroom_options == "stand on stool"):
        print("""You stand on the stool, there isn't much else to see apart from what you could 
already see but you can now reach the vent.""")
        bathroom_stool_scene()  # goes back to the beginning of the scene

    elif stool_in_bathroom is True and (bathroom_options == "use stool" or bathroom_options == "stand on stool"):
        print("""You stand on the stool, there isn't much else to see apart from what you could 
already see but you can now reach the vent.""")
        bathroom_stool_scene()  # goes back to the beginning of the scene

    elif "stool" not in inventory and (bathroom_options == "use stool" or bathroom_options == "stand on stool"):
        print("You do not have a stool.")
        bathroom_scene_restart()  # goes back to the beginning of the scene

    elif bathroom_options == "help":  # if help is entered it will carry out these functions:
        print(help_guide)  # displays help guide
        bathroom_scene_restart()  # goes back to the beginning of the scene

    elif bathroom_options == "inventory":  # if inventory is entered it will carry out these functions:
        print(inventory)  # displays the inventory guide
        bathroom_scene_restart()  # goes back to the beginning of the scene

    else:  # if no other option is fitting it will carry out these functions:
        print("I do not understand, type help for general instructions.")  # asking the player to reenter
        bathroom_scene_restart()  # goes back to the beginning of the scene


def cupboard_scene_restart():  # defining the point in which players return to after completing an action

    global flashlight_with_batteries  # declares the global flashlight with batteries variable within this scene
    cupboard_options = input("What would you like to do? ").lower()  # gets the players input
    if cupboard_options == "west":  # if west is entered it will carry out these functions:
        starting_room_scene()  # will return the player to the starting room

    elif cupboard_options == "examine stool":  # if help is entered it will carry out these functions:
        print("""The stool is very obviously old and well used, it's three legs are sturdy. They have probably been
replaced multiple times each leg is a different colour of wood. It could take your weight. You decide to take it with 
you, it might be useful.
""")  # displays the description
        inventory.append("stool")  # adds stool to the inventory
        cupboard_scene_restart()  # goes back to the beginning of the scene

    elif cupboard_options == "examine boxes":  # if help is entered it will carry out these functions:
        print("""The boxes are pretty full, though most are half bubble wrap and half different plates, bowls and cups 
though in the bottom of one you find a flashlight and in another a first aid kit. You shove both in your pocket, you're
glad you are wearing mens clothes so that this can fit.""")  # displays the description
        inventory.append("flashlight")  # adds flashlight to the inventory
        inventory.append("first aid kit")  # adds first aid kit to the inventory

        # if the flashlight and batteries are in the inventory it will carry out these functions:
        if (inventory == "flashlight" and "batteries") and flashlight_with_batteries is False:
            print("You take a moment to put the batteries in the flashlight.")  # displays the description
            inventory.remove("batteries")  # removes batteries from inventory
            flashlight_with_batteries = True  # sets the flashlight with batteries variable as true
            cupboard_scene_restart()  # goes back to the beginning of the scene

        else:  # if no other option is fitting it will carry out these functions:
            cupboard_scene_restart()  # goes back to the beginning of the scene

    elif cupboard_options == "help":  # if help is entered it will carry out these functions:
        print(help_guide)  # displays help guide
        cupboard_scene_restart()  # goes back to the beginning of the scene

    elif cupboard_options == "inventory":  # if inventory is entered ut will carry out these functions:
        print(inventory)  # displays the inventory guide
        cupboard_scene_restart()  # goes back to the beginning of the scene

    else:  # if no other option is fitting it will carry out these functions:
        print("I do not understand, type help for general instructions.")  # asking the player to reenter
        cupboard_scene_restart()  # goes back to the beginning of the scene


# the scene for the bathroom but the player is stood on a stool
def bathroom_stool_scene():
    global vent_opened  # declares the global vent opened variable within this scene
    global stool_in_bathroom  # declares the global stool in bathroom variable within this scene
    stool_in_bathroom = True  # sets the stool in bathroom variable as true
    stool_options = input("What would you like to do?")  # gets the players input

    # if use screwdriver is entered and it is in the inventory it will carry out these functions:
    if "screwdriver" in inventory and stool_options == "use screwdriver":
        screwdriver_use = input("What would you like to use the screwdriver on? ")  # gets the players input

        # if vent is entered and the vent hasn't been opened it will carry out these functions:
        if screwdriver_use == "vent" and vent_opened is False:
            print("""You start unscrewing the vent, the screws are rusted so it takes a lot of effort but eventually all
four come out and you are able to pop the vent front off of the wall. You look around inside but you can't see much, you
reach your hand in but it goes straight into a spiders web. Still you search around a bit and manage to pull out a key. 
Weird.""")  # displays the description
            inventory.append("key")  # adds the key to the inventory
            bathroom_stool_scene()  # goes back to the beginning of the scene

        # if vent is entered and the vent has been opened it will carry out these functions:
        elif screwdriver_use == "vent" and vent_opened is True:
            print("The vent is already open")  # displays the description
            bathroom_stool_scene()  # goes back to the beginning of the scene

    # if open vent is entered, and it has not been opened it will carry out these functions:
    elif stool_options == "open vent" and vent_opened is False:
        open_vent = input("The vent is screwed shut, what would you like to use to open it? ")
        if open_vent == "screwdriver" and "screwdriver" in inventory:
            print("You unscrew the vent")  # displays the description
            bathroom_stool_scene()  # goes back to the beginning of the scene

    # if open vent is entered, and it has been opened it will carry out these functions:
    elif stool_options == "open vent" and vent_opened is True:
        print("The vent is already open.")  # displays the description
        bathroom_stool_scene()  # goes back to the beginning of the scene

    elif stool_options == "get off stool":  # if 'get off stool' is entered it will carry out these functions:
        print("""You step off of the stool. It wobbles as you do causing you to almost fall, you're glad no one was here
to see that. You leave the stool here.""")  # displays the description
        inventory.remove("stool")  # removes the stool from the inventory
        bathroom_scene_restart()  # goes back to the beginning of the bathroom scene

    elif stool_options == "help":  # if help is entered it will carry out these functions:
        print(help_guide)  # displays help guide
        bathroom_stool_scene()  # goes back to the beginning of the scene

    elif stool_options == "inventory":  # if inventory is entered it will carry out these functions:
        print(inventory)  # displays the inventory guide
        bathroom_stool_scene()  # goes back to the beginning of the scene

    else:  # if no other option is fitting it will carry out these functions:
        print("I do not understand, type help for general instructions")  # asking the player to reenter
        print("Perhaps try 'get off stool' if you are really stuck")  # giving a hint to get off the stool
        bathroom_stool_scene()  # goes back to the beginning of the scene


# all scenes that include the descriptions of the room
def cupboard_scene():  # defining the cupboard scene
    print(cupboard_description)  # displays the cupboard description
    print("")
    cupboard_scene_restart()  # starts the cupboard scene from a point that doesn't include the room descriptions


def starting_room_scene():  # defining the starting room scene
    print(starting_room_description)  # displays the starting room description
    print("")
    starting_room_scene_restart()  # starts the starting scene from a point that doesn't include the room descriptions


def bathroom_scene():  # defining the bathroom scene
    print(bathroom_description)  # displays the bathroom description
    print("")
    bathroom_scene_restart()  # starts the bathroom scene from a point that doesn't include the room descriptions


def kitchen_scene():  # defining the kitchen scene
    print(kitchen_description)  # displays the kitchen description
    print("")
    kitchen_scene_restart()  # starts the kitchen scene from a point that doesn't include the room descriptions


print(opening_text)  # displays the opening text which is defined earlier
starting_room_scene()  # starts the starting scene
