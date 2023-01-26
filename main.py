import random
import sys
import time

inventory = ["knife"]  # inventory list
obtained_items = []
weapons_avaliable = ["knife", "shovel", "crowbar", "ore"]
weapon_damage = {"knife": 25, "shovel": 35, "crowbar": 30, "ore": 20}
player_health = 150  # player health
got_map = True  # has map

typing_speed = 10000  # amount of words per minute


def slow_type(text):  # defining text typing out slowly
    for letters in text:  # will do this for all letters in the text
        sys.stdout.write(letters)  # will write out letter by letter
        sys.stdout.flush()  # clears the internal buffer of the file
        time.sleep(random.random() * 10.0 / typing_speed)  # how quickly the text will type


# enemy class
class Enemy:
    def __init__(self, health, name, weapon, attack):
        self.health = health
        self.name = name
        self.weapon = weapon
        self.attack = attack


enemy_1 = Enemy(100, "Monster", "Fangs", random.randrange(10, 30))
enemy_2 = Enemy(100, "Bugbear", "Tree Log", random.randrange(10, 30))
enemy_3 = Enemy(150, "Karkinos", "Claws", random.randrange(10, 30))

# variables for outside the house
glove_box_opened = False
boat_unlocked = True
boat_code = "dtbcbv"
grave_dug = False
check = any(item in inventory for item in weapons_avaliable)

# variables for inside the house
door_locked = True  # sets the main door as locked
box = False  # sets the box in the kitchen as closed
bedside_draw = False  # sets the bedside table in the starting room draws as closed
safe_code = []  # list for the safe code in the bathroom once it has been randomly chosen
codes_cracked = 0  # the amount of successful attempts there have been to open the bathroom safe
safe_opened = False  # sets the bathroom safe as closed
vent_opened = False  # sets the bathroom vent as closed
stool_in_bathroom = False  # sets the stool in the bathroom as no
flashlight_with_batteries = False  # sets the flashlight with batteries as no
fireplace_lighted = False  # sets the fireplace as unlighted
campfire_lighted = False  # sets the campfire as unlighted

# outside map
player_map = """ 
\033[1;37;40m         _____              \033[0;39m
\033[1;37;40m   \    |_____|     |__/    \033[0;39m
\033[1;37;40m   _|_____| |_______|____   \033[0;39m
\033[1;37;40m  /  ______   ____   ____|  \033[0;39m
\033[1;37;40m  | |      | |    | |       \033[0;39m
\033[1;37;40m  _____     \ \   / /       \033[0;39m
\033[1;37;40m |_____|     \  v  /----    \033[0;39m
\033[1;37;40m _____________|   |________ \033[0;39m
\033[1;34;40m ~~~~~~~~~~~~~~~~~~~~~~~~~~ \033[0;39m          
"""

# outside descriptions
outside_1_description_with_enemy = """The dirt path leads you through some trees, theres not much around as you push the 
branches out of the way. An opening is presented to you. A circle where trees once would have been but have been cut 
down and the stumps dug up. The path continues but a hunch over shadow is at the end. You aren't sure what it is but
but the monsters body visibly expands with each and every exhale. A bone chilling growl vibrates through your body. You 
stumble back, breath catching in your throat."""

outside_1_description_without_enemy = """The dirt path leads you through some trees, theres not much around as you push 
the branches out of the way. An opening is presented to you. A circle where trees once would have been but have been 
cut down and the stumps dug up. A body of the beast you slayed slumped in the middle, you almost feel bad for it.

Almost."""

outside_2_shack_description = """The outside of the shack is as run down as the inside. The wood is all mismatched and 
half broken from repairs over the year. The basement you were in is not what you would think was inside. The complete
contrast makes the whole building creepier. You really should get out of here."""

outside_3_description_with_enemy = """Up ahead the dirt path splits into two. If you continued forward you can see the 
end but to the right you can't quite see due to the trees blocking it. Theres a... monster, or maybe a rabid animal, or
something up ahead. It looks not quite human and  not quite animal and not quite right either. You remember a monster 
from a book you read as a kid... it sort of looks like a Bugbear"""

outside_3_description_without_enemy = """Up ahead the dirt path splits into two. If you continued forward you can see 
the end but to the right you can't quite see due to the trees blocking it. The body of the monster is crumpled at the 
end of the path."""

outside_4_description = """An outhouse sits at the end of the path. As run down as the shack, much smaller too. The door 
is half hanging off so you can see the hole in the ground and can tell that it's supposed to be a toilet. You would not 
use bit if your life depended on it."""

outside_5_description = """The path continues on to the north but to the south there is a dirt path that heads off into 
the trees. The gap isn’t big enough for you to see through it but big enough for you to walk through. There are some 
bushes on the outskirts of the trees, there is a weird gap in one of the bushes. Almost as if something, maybe a 
squirrel, has been in it. 
"""

outside_6_crossroads_description = """You come to a crossroad, you can't quite tell where each place goes apart from the 
shack to the \033[1;92mSouth\033[0;39m. There is no sign in sight telling you where you can go. You think there might've
been one at some point, however as there is a car crashed into what can only be an old sign post you recon it's going
to be pretty useless now."""

outside_7_T_junction_description = """The path leads into a t-junction. Off to the \033[1;92mSouth\033[0;39m there is a 
dirt path that isn't part of the path but made over years of people walking there so much the grass has died. You can't 
see any signs hidden in the trees, nor in the bushes. It's suspiciously empty here..."""

outside_8_graveyard_description = """The path leads you to a graveyard. Rows of headstones lay in front of you, all 
varying in quality and how well looked after they are. The row you are closest to is very obviously the newest set of 
graves. Some have not been there long enough for even mother nature to touch them. At the end of the front row there is 
an empty grave, freshly dug. To the left of the path there is a grave out of place, the headstone is blank. The nameless 
grave, from what you can tell, has been dug up again and again though you are not sure why. 	
"""

outside_9_building_description = """At the end of the path there is a building. The walls and roof are half missing, 
windows all smashed in. The door swings side to side with a quiet creek with each swish of the wind. You cannot tell 
what is inside but the outside has clearly succumbed to the elements over the years. 
"""

outside_10_description = """The area you enter is pretty empty, bushes and trees surrounding the bend in the path. You 
look around, there are wooden planks buried in the dirt that act as stairs to combat the slope of the ground. One of the
planks juts out of the ground unnaturally, it's thinner than the rest and you almost trip when you try to step on it. 
You are glad that you don't because you're pretty sure that there is a patch of stinging nettles next to it."""

outside_11_split_path_description = """You come to a split in the path. One way goes to the \033[1;92mSouth\033[0;39m
one to the \033[1;92mEast\033[0;39m and the final way goes down to the \033[1;92mNorth\033[0;39m. As most places you've
been there are trees and bushes surrounding the path, everywhere in this stupid place looks the same."""

outside_12_description_with_enemy = """A small gap in the trees reveals a dirt path, it hasn't been walked much. Grass 
threatens to peak through and hide it completely but you decide to walk it anyway. You push your way through and come to 
an opening no bigger than the room you woke up in. On the far side hidden amongst the trees red eyes glare at you, it's 
hard to tell what it is exactly but you can see it's crab like claws that are half the size of you. From what you can
tell it sort of looks like a Karkinos."""

outside_12_description_without_enemy = """A small gap in the trees reveals a dirt path, it hasn't been walked much. 
Grass threatens to peak through and hide it completely but you decide to walk it anyway. You push your way through and 
come to an opening no bigger than the room you woke up in. In the center remains the corpse of the Karkinos you killed. 

You're glad it's still dead."""

lake_description = """The path leads you to an opening, a lake is ahead of you. It goes on for miles and you can only 
see the other side when straining your eyes. Theres no trees there, you recon that's your best shot of getting out of 
here. Looking around the area you are in is the only one that it completely blocked off by trees and where the water is
not too deep to walk in. There is an abandoned boat just this side of the trees and there is rubbish littered across
what little of the beach there is."""

# opening descriptions
opening_text = """You awaken in a room that you do not recognise with no memories on how you got here, you remember most 
of yesterday but after leaving work in the evening it all goes blank. You should probably get out of here, your cat will 
be hungry if you don't get home soon. when you think about it you're not sure what time it is nor how long you've been 
asleep.  
"""

# different rooms in the house descriptions
# \033[1;92m turns the text green \033[0;39m turns it back.
starting_room_description = """The room is dim but you can make out a door on each wall that lead to different rooms.
There are no windows. To the\033[1;92m South\033[0;39m is the kitchen, if the counters and fridge you can see are 
anything to go off of. The door to the\033[1;92m East\033[0;39m is a cupboard, and the\033[1;92m west\033[0;39m is the 
bathroom.The door to the\033[1;92m North\033[0;39m seems to be the main door, there is a padlock keeping it locked shut. 
You are on the bed, it is perfectly made apart from where you've moved it as you got up. There are two
bedside tables, one contains a lamp both have draws that are currently shut."""

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

going_up_stairs_description = """The stairs, unlike everything you've seen so far, are extremely run down and dirty. 
They creek awfully when you go up and ring in your ear against the complete silence otherwise. Each step feels like a 
step towards death."""

going_down_stairs_description = """Going back down the stairs feels as dreadful as going up and safe all at once. The 
familiarity of it all is comforting... 
You really need to get out of here."""

upstairs_description = """Similar to the stairs the upstairs room is dingy, gross and just a little too empty. Theres an 
unlit campfire in the corner despite the fireplace directly in the middle of the wall opposite you. Next to the campfire 
is a crowbar. The door is to the\033[1;92m North\033[0;39m. There is a bookshelf with a few books that are all old and 
dusty. You cannot see anything else in the room."""

# basic help guide of commands that can be written
# /033[0;31m and /n make the text appear red
help_guide = """\033[1;31m
- Basic commands: 
- 'north', 'south', 'east', 'west' to move around the rooms. 
- use [item] to use something.
- examine [object] to get a closer look.
- enter [place] to enter places. most places will use direction to enter however this is also used.
- inventory to open your inventory.
- map to see your map.\n \033[0;39m \n"""  # \033[0;39m \n turns it back to white


# the point in scenes the player will go back to when an action is completed
# in order to stop them from having to read the descriptions each time
# all of theses are for inside the house
def starting_room_scene():  # defining the point in which players return to after completing an action

    print("")  # blank print for formatting
    slow_type(starting_room_description)  # displays the starting room description
    print("")  # blank print for formatting

    global bedside_draw  # declares the global bedside_draw variable within this scene
    global flashlight_with_batteries  # declares the global flashlight with batteries variable within this scene
    global door_locked  # declares the global door locked variable within this scene
    global got_map  # declares the map in the scene

    while True:

        print("")  # blank print for formatting
        starting_room_options = input("what would you like to do? ").lower()  # gets the players input
        # . lower() changes anything entered to lowercase
        print("")  # blank print for formatting

        if starting_room_options == "east":  # if south is entered it will carry out these functions:
            cupboard_scene()  # starts the cupboard scene

        elif starting_room_options == "south":  # if south is entered it will carry out these functions:
            kitchen_scene()  # starts the kitchen scene

        elif starting_room_options == "west":  # if west is entered it will carry out these functions:
            bathroom_scene()  # starts the bathroom scene

        # if north is entered and the door is locked it will carry out these functions:
        elif starting_room_options == "north" and door_locked is True:
            if "key" in inventory:
                slow_type("The door is padlocked shut, you pull at the handle. It doesn't move.You have a key on you")
                print("")  # blank print for formatting

                while True:  # will happen while
                    print("")  # blank print for formatting
                    key = input("would you like to use it? ")
                    print("")  # blank print for formatting

                    if key == "yes":
                        # displays the description:
                        slow_type("The lock clicks open and you are able to pull it off and open the door.")
                        inventory.remove("key")
                        door_locked = False
                        break

                    elif key == "no":
                        slow_type("The lock stays locked.")  # displays the description
                        break

                    else:  # if no other option is fitting it will carry out these functions:
                        # asking the player to reenter
                        print("I do not understand, type help for general instructions.")

            else:
                # displays the description:
                slow_type("The door is padlocked shut, you pull at the handle. It doesn't move.")

        # if north is entered and the door is locked it will carry out these functions:
        elif starting_room_options == "north" and door_locked is False:
            slow_type(going_up_stairs_description)  # displays the description
            upstairs_scene()  # starts the upstairs scene

        elif starting_room_options == "examine bed":  # if bed is entered it will carry out these functions:
            slow_type("""Other then where you were sleeping the bed is made perfectly, you crouch down and under the bed
it is empty, it looks as though something was once there but whatever it was is gone. It's dusty, the dirtiest thing 
you've seen so far. whatever was there was dragged out recently.""")  # displays the description

        # if examine bedside table(s) is entered it will carry out these functions:
        elif starting_room_options == "examine bedside table" or starting_room_options == "examine bedside tables":
            slow_type("""Both bedside tables, like everything in the room, look new. One contains a lamp, it doesn't 
work when you pull it. There is one draw in both beside tables""")  # displays the description

        elif starting_room_options == "examine lamp":  # if examine lamp is entered it will carry out these functions:
            slow_type("""Upon closer inspection on the lamp you realise that where you though it was a normal lamp it is
in fact a horse. A horse with a lampshade on its head, you aren't sure where the on switch is and are kind of scared to 
find out. It's actually pretty cool, you consider buying one but as you're inspecting it you see the price tag. £5,509. 
You put it back down, maybe not then.""")  # displays the description

        # if examine padlock is entered it will carry out these functions:
        elif starting_room_options == "examine padlock":
            slow_type("""The padlock needs key to unlock it, out of everything you've seen so far it's the most well 
used. It has scratches covering it as though someones been yanking it, or at the very least has had it attached to 
something that bashed it about a lot.""")  # displays the description

        # if the beside draws have yet to be opened it will carry out these functions:
        elif (starting_room_options == "use draws" or starting_room_options == "open draws") and bedside_draw is False:
            slow_type("""when you check both draws one contains two batteries, the other empty. You shove the batteries 
into your pocket and shut the draws.""")  # displays the description
            inventory.append("batteries")  # adds batteries to the inventory
            bedside_draw = True  # sets the beside draws as open

            # if the flashlight and batteries are in the inventory it will carry out these functions:
            if (inventory == "flashlight" and "batteries") and flashlight_with_batteries is False:
                slow_type("You take a moment to put the batteries in the flashlight.")  # displays the description
                inventory.remove("batteries")  # removes batteries from inventory
                flashlight_with_batteries = True  # sets the flashlight with batteries variable as true

            else:  # if no other option is fitting it will carry out these functions:
                print("")

        # beside draw function but non-plural
        elif (starting_room_options == "use draw" or starting_room_options == "open draw") and bedside_draw is False:
            slow_type("""when you check both draw one contains two batteries, the other empty. You shove the batteries 
into your pocket and shut the draws.""")  # displays the description
            inventory.append("batteries")  # adds batteries to the inventory
            bedside_draw = True  # sets the beside draws as open

            # if the flashlight and batteries are in the inventory it will carry out these functions:
            if (inventory == "flashlight" and "batteries") and flashlight_with_batteries is False:
                slow_type("You take a moment to put the batteries in the flashlight.")  # displays the description
                inventory.remove("batteries")  # removes batteries from inventory
                flashlight_with_batteries = True  # sets the flashlight with batteries variable as true

            else:  # if no other option is fitting it will carry out these functions:
                print("")

        # if the beside draw has been opened it will carry out these functions:
        elif (starting_room_options == "use draw" or starting_room_options == "open draw") and bedside_draw is True:
            slow_type("when you open the draws they are both empty.")  # displays the description

        elif starting_room_options == "use key" and "key" in inventory:
            print("")  # blank print for formatting
            key = input("what would you like to use it on? ")
            print("")  # blank print for formatting

            if key == "door":
                slow_type("The lock clicks open and you are able to pull it off and open the door.")
                inventory.remove("key")

            else:
                print("You can not use the key there.")

        elif starting_room_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays the help guide

        elif starting_room_options == "inventory":  # if inventory is entered it will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif starting_room_options == "map" and got_map is True:
            print(player_map)  # displays the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif starting_room_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions::
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def kitchen_scene():
    print("")  # blank print for formatting
    slow_type(kitchen_description)  # displays the kitchen description
    print("")  # blank print for formatting

    global box  # declares the global box variable within this scene
    global got_map  # declares the map in the scene

    while True:

        print("")  # blank print for formatting
        kitchen_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if kitchen_options == "north":  # if south is entered it will carry out these functions:
            starting_room_scene()  # will return the player to the starting room

        elif kitchen_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif kitchen_options == "south":  # if west is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif kitchen_options == "west":  # if south is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif box is False and kitchen_options == "examine box":  # checks if the box has been opened
            slow_type("""The box is just big enough to hold a handful of golf balls, the design is very detailed but a 
little ugly.""")  # displays the description

        elif box is True and kitchen_options == "examine box":  # checks if the box has been opened
            slow_type("The box remains open on the table, it is empty.")  # displays the description

        elif kitchen_options == "examine fridge":  # if examine fridge is entered it will carry out these functions:
            slow_type("""Unlike the cupboards the fridge is not well stocked, there is a few bottles of water on one of 
the shelves. The first one you pick up has been opened and is missing some water. The rest have not been. when the water 
is in your hand you notice that it is far too warm for being in the fridge.""")  # displays the description

        elif kitchen_options == "examine chair":  # if examine chair is entered it will carry out these functions:
            slow_type("""The chair is nothing special but if you stood on the chair you would be able to see out the 
little window, it seems practically new.""")  # displays the description

        elif kitchen_options == "examine window":  # if examine window is entered it will carry out these functions:
            slow_type("""You are unable to see out of the window from here, when you stand back you are able to see the 
sky but you can't quite tell what time it is.""")  # displays the description

        elif kitchen_options == "examine table":  # if examine table is entered it will carry out these functions:
            slow_type("""The table looks somewhat new, there are scratches on the edge you can't tell what made them. 
There is a box sitting in the middle if not a little closer to the left side. The table is made of wood unlike the chair 
tucked under it which is made out of metal.""")  # displays the description

        elif kitchen_options == "examine oven":  # if examine oven is entered it will carry out these functions:
            slow_type("""From what you can tell the oven is gas, you reach out and try to turn it on but nothing you do
works. when you try to pull open the main oven it won't move no matter how hard you pull it as if someone has glued it 
shut.""")  # displays the description

        # if examine cupboard is entered it will carry out these functions:
        elif kitchen_options == "examine cupboards" or kitchen_options == "examine cupboard":
            slow_type("""Upon further inspection while the cupboards appear to be well stocked everything has been
pulled to the front edge of them. You pick up the closest can and realise it's empty. You replace it in the cupboard and 
pick up another, it's also empty.""")  # displays the description

        # if stand on chair or use chair is entered it will carry out these functions:
        elif kitchen_options == "stand on chair" or kitchen_options == "use chair":
            slow_type("""You climb onto the chair, it rocks gently beneath you and creaks loudly in the silent room but 
you hold out your arms to balance yourself. bOnce you are up there you can't see anything new in the room but you are 
able to see out the little window. From what you can tell you must be in a basement since you can only see the bottom of 
trees from your position. Even from up here you cant quite tell what time it is.""")  # displays the description

            # if open box or use box is entered and the box hasn't been opened it will carry out these functions:
        elif (kitchen_options == "use box" or kitchen_options == "open box") and box is False:
            slow_type("""You reach into the box and there sits a rusted, falling apart screwdriver. It's kind of a weird 
place to keep it, instead of thinking to hard about the really strange place to keep a tool you shove it into your 
pocket for later use.""")  # displays the description
            inventory.append("screwdriver")  # adds the screwdriver to the inventory
            box = True  # sets the box to true to confirm it's been opened

        # if open box or use box is entered and the box has been opened it will carry out these functions:
        elif (kitchen_options == "use box" or kitchen_options == "open box") and box is True:
            slow_type("The box is empty, you already took the screwdriver from it.")  # displays the description

        elif kitchen_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)

        elif kitchen_options == "inventory":  # if inventory is entered it will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif kitchen_options == "map" and got_map is True:
            print(player_map)  # displays the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif kitchen_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def bathroom_scene():
    print("")  # blank print for formatting
    slow_type(bathroom_description)  # displays the bathroom description
    print("")  # blank print for formatting

    global safe_opened  # declares the global safe opened variable within this scene
    global stool_in_bathroom  # declares the global stool in bathroom variable within this scene
    global got_map  # declares the map in the scene

    while True:

        print("")  # blank print for formatting
        bathroom_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if bathroom_options == "north":  # if south is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif bathroom_options == "east":  # if east is entered it will carry out these functions:
            starting_room_scene()  # will return the player to the starting room

        elif bathroom_options == "south":  # if west is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif bathroom_options == "west":  # if south is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif bathroom_options == "examine shower":  # if examine shower is entered it will carry out these functions:
            slow_type("""It's one of those showers that is shoved into the corner of the room and would usually have two 
glass doors that open on the corner but instead it is two shower curtains, when you push them back there are a range of 
shower products. A weird amount really.""")  # displays the description

        elif bathroom_options == "examine toilet":  # if examine toilet is entered it will carry out these functions:
            slow_type("""Upon closer inspection you think, wow, that sure is a toilet. It might possibly be the most 
average toilet you've ever seen.""")  # displays the description

        elif bathroom_options == "examine sink":  # if examine sink is entered it will carry out these functions:
            slow_type("""If a sink could appear in the dictionary next to the word sink there is a real chance it could 
be this one. It is a picture perfect sink.""")  # displays the description

        elif bathroom_options == "examine vent":  # if examine vent is entered it will carry out these functions:
            slow_type("The vent is pretty high up, you can't quite reach it from here.")  # displays the description

        # if examine toothbrushes is entered it will carry out these functions:
        elif bathroom_options == "examine toothbrushes":
            slow_type("""Three toothbrushes sit in a pot, they're the only things in there. There's a green, blue and 
purple one. The green has obviously been use, though it's unclear how recently.""")  # displays the description

        elif bathroom_options == "examine mat":  # if examine padlock is entered it will carry out these functions:
            slow_type("""while it's obviously supposed to be white you can tell even from the door that it's greying 
from use. It's bone dry, well dead bone dry, alive bones are actually wet. You don't really think much of the mat though 
it looks as though there is something underneath.""")  # displays the description

        # if examine use mat or move mat is entered will carry out these functions:
        elif bathroom_options == "use mat" or bathroom_options == "move mat":
            slow_type("""when you move the mat theres a safe underneath, you aren't sure what the code is but theres 
tree notes on the bottom of the mat it read:""")  # displays the description

            if safe_opened is False:  # if safe has not been opened carry out these functions:
                global safe_code  # declares the global safe code variable within this scene
                while len(safe_code) < 1:  # checks how many successful attempt there have already been
                    code = random.randint(3, 12)  # randomises what numbers the is, between 3 and 12
                    if code not in safe_code:  # checks to see if the number has already been chosen
                        safe_code.append(code)  # adds the number to the code list if they haven't already been used
                    global codes_cracked  # declares the global code cracked variable within this scene

                    # while the number of successful attempts is less than three the code will repeat
                    while codes_cracked < len(safe_code):
                        # tells the player what to do
                        slow_type("you must enter a pair of numbers that divide to %d." % code)
                        try:  # catches errors, instead of stopping the code it reruns
                            player_number_1 = float(input("Enter number: "))  # asking the player to enter a number
                            player_number_2 = float(input("Enter number: "))  # asking the player to enter a number
                            result = player_number_1 // player_number_2  # divides the numbers given
                            if result == code:  # if the result is the same as the code these functions will happen:
                                slow_type("Correct.")  # confirms the guess was correct
                                codes_cracked += 1  # adds 1 to the amount of successful attempts

                        except ValueError:  # if the player enters anything but a number these functions will happen:
                            print("Not a number.")  # confirms it is not a number
                            break  # stops the loop and skip to the next code after the loo

                        except ZeroDivisionError:  # if the player enters 0 these functions will happen:
                            print("Can't divide by zero.")  # confirms they cannot divide by 0

                    else:
                        slow_type("You have opened the safe.")  # displays the description
                        slow_type("""You think it's kind of weird that whoever lives here put the code to the safe on 
the mat hiding it, and even weirder they did it as a riddle, but it works out for you because it clicks open and you are 
able to reach in and pull out a... you can't actually tell what it is. It's paper, green, kind of crushed. It might be a
frog? Judging by the eyes and weird uneven legs. A solid attempt, just not a great one. The state of it makes you feel 
less guilty when you unfold it and find a singular word written on it: Fireplace... 
what does that mean?
""")  # displays the description

            elif safe_opened is True:  # of safe has been opened carry out these functions:
                slow_type("The safe is unlocked but close. It remains empty.")

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif "stool" in inventory and (bathroom_options == "use stool" or bathroom_options == "stand on stool"):
            slow_type("""You stand on the stool, there isn't much else to see apart from what you could 
    already see but you can now reach the vent.""")
            bathroom_stool_scene()  # goes back to the beginning of the scene

        elif stool_in_bathroom is True and (bathroom_options == "use stool" or bathroom_options == "stand on stool"):
            slow_type("""You stand on the stool, there isn't much else to see apart from what you could 
    already see but you can now reach the vent.""")
            bathroom_stool_scene()  # goes back to the beginning of the scene

        elif "stool" not in inventory and (bathroom_options == "use stool" or bathroom_options == "stand on stool"):
            slow_type("You do not have a stool.")

        elif bathroom_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif bathroom_options == "inventory":  # if inventory is entered it will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif bathroom_options == "map" and got_map is True:
            print(player_map)  # displays the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif bathroom_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def bathroom_stool_scene():  # the scene for the bathroom but the player is stood on a stool

    global vent_opened  # declares the global vent opened variable within this scene
    global stool_in_bathroom  # declares the global stool in bathroom variable within this scene
    global got_map  # declares the map in the scene
    stool_in_bathroom = True  # sets the stool in bathroom variable as true

    while True:

        print("")  # blank print for formatting
        stool_options = input("what would you like to do?")  # gets the players input
        print("")  # blank print for formatting

        # if use screwdriver is entered and it is in the inventory it will carry out these functions:
        if "screwdriver" in inventory and stool_options == "use screwdriver":
            screwdriver_use = input("what would you like to use the screwdriver on? ")  # gets the players input

            # if vent is entered and the vent hasn't been opened it will carry out these functions:
            if screwdriver_use == "vent" and vent_opened is False:
                slow_type("""You start unscrewing the vent, the screws are rusted so it takes a lot of effort but 
eventually all four come out and you are able to pop the vent front off of the wall. You look around inside but you 
can't see much, you reach your hand in but it goes straight into a spiders web. Still you search around a bit and manage 
to pull out a key. 
weird.""")  # displays the description
                inventory.append("key")  # adds the key to the inventory

            # if vent is entered and the vent has been opened it will carry out these functions:
            elif screwdriver_use == "vent" and vent_opened is True:
                slow_type("The vent is already open")  # displays the description

        # if open vent is entered, and it has not been opened it will carry out these functions:
        elif stool_options == "open vent" and vent_opened is False:
            open_vent = input("The vent is screwed shut, what would you like to use to open it? ")
            if open_vent == "screwdriver" and "screwdriver" in inventory:
                slow_type("You unscrew the vent")  # displays the description
                bathroom_stool_scene()  # goes back to the beginning of the scene

        # if open vent is entered, and it has been opened it will carry out these functions:
        elif stool_options == "open vent" and vent_opened is True:
            slow_type("The vent is already open.")  # displays the description
            bathroom_stool_scene()  # goes back to the beginning of the scene

        elif stool_options == "get off stool":  # if 'get off stool' is entered it will carry out these functions:
            slow_type("""You step off of the stool. It wobbles as you do causing you to almost fall, you're glad no one 
was here to see that. You leave the stool here.""")  # displays the description
            inventory.remove("stool")  # removes the stool from the inventory

        elif stool_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif stool_options == "inventory":  # if inventory is entered it will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif stool_options == "map" and got_map is True:
            print(player_map)  # displays the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif stool_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            slow_type("I do not understand, type help for general instructions")  # asking the player to reenter
            slow_type("Perhaps try 'get off stool' if you are really stuck")  # giving a hint to get off the stool


def cupboard_scene():  # defining the point in which players return to after completing an action

    print("")  # blank print for formatting
    slow_type(cupboard_description)  # displays the cupboard description
    print("")  # blank print for formatting

    global flashlight_with_batteries  # declares the global flashlight with batteries variable within this scene
    global got_map  # declares the map in the scene

    while True:

        print("")  # blank print for formatting
        cupboard_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if cupboard_options == "north":  # if south is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif cupboard_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif cupboard_options == "south":  # if west is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif cupboard_options == "west":  # if west is entered it will carry out these functions:
            starting_room_scene()  # will return the player to the starting room

        elif cupboard_options == "examine stool":  # if help is entered it will carry out these functions:
            slow_type("""The stool is very obviously old and well used, it's three legs are sturdy. They have probably 
been replaced multiple times each leg is a different colour of wood. It could take your weight. You decide to take it 
with you, it might be useful.
    """)  # displays the description
            inventory.append("stool")  # adds stool to the inventory

        elif cupboard_options == "examine boxes":  # if help is entered it will carry out these functions:
            slow_type("""The boxes are pretty full, though most are half bubble wrap and half different plates, bowls 
and cups though in the bottom of one you find a flashlight and in another bandages. You shove both into your 
pocket, you're glad you are wearing mens clothes so that this can fit.""")  # displays the description
            inventory.append("flashlight")  # adds flashlight to the inventory
            inventory.append("bandages")  # adds bandages to the inventory

            # if the flashlight and batteries are in the inventory it will carry out these functions:
            if (inventory == "flashlight" and "batteries") and flashlight_with_batteries is False:
                slow_type("You take a moment to put the batteries in the flashlight.")  # displays the description
                inventory.remove("batteries")  # removes batteries from inventory
                flashlight_with_batteries = True  # sets the flashlight with batteries variable as true

            else:  # if no other option is fitting it will carry out these functions:
                print("")

        elif cupboard_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif cupboard_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif cupboard_options == "map" and got_map is True:
            print(player_map)  # displays the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif cupboard_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def upstairs_scene():
    global got_map  # declares the map in the scene
    global fireplace_lighted  # declares the fireplace lighted in the scene
    global campfire_lighted  # declares the campfire lighted in the scene

    print("")  # blank print for formatting
    slow_type(upstairs_description)  # displays the upstairs description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        upstairs_options = input("What would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if upstairs_options == "north":  # if south is entered it will carry out these functions:
            slow_type("""You reach for the handle, take a deep breath and hope you know where you are when you leave. 
You've never been particularly lucky though.""")
            outside_2_shack_scene()

        elif upstairs_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        elif upstairs_options == "south":  # if south is entered it will carry out these functions:
            slow_type(going_down_stairs_description)  # displays the description
            starting_room_scene()  # goes back to the starting room scene

        elif upstairs_options == "west":  # if west is entered it will carry out these functions:
            print("You cannot go that way.")  # lets the player know there is no path there

        # if examine crowbar is entered it will carry out these functions:
        elif upstairs_options == "examine crowbar" and "crowbar" not in inventory:
            slow_type("""The crowbar is old and rusted but sturdy. You doubt it will break anytime soon and trust it 
could do some damage. """)  # displays the description
            crowbar = input("Would you like to take it with you? ")  # gets the players input
            if crowbar == "yes":  # if yes is entered it will carry out these functions:
                inventory.append("crowbar")  # adds crowbar to inventory
                slow_type("You take the crowbar and hang it on your belt.")

            elif crowbar == "no":  # if no is entered it will carry out these functions:
                slow_type("You put the crowbar back where you found it.")  # displays the description

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif upstairs_options == "examine crowbar" and "crowbar" in inventory:
            print("You already have the crowbar")  # displays the description

        elif upstairs_options == "examine campfire" and campfire_lighted is False:
            slow_type("""The campfire, upon further inspection, has been lit somewhat recently. You hover your hand over 
it and it feels warm. You looked around, theres still no one here. Weird.""")

        elif upstairs_options == "examine fireplace" and fireplace_lighted is False:
            slow_type("""The fireplace hasn't been lit for a while. The ash has long gone cold, enough for you to be 
able to touch it without an issue. You recon theres probably something around here that you could use to light it.""")

        elif upstairs_description == "examine campfire" and campfire_lighted is True:
            slow_type("The campfire has been lighted recently, though unlike before you know who did it.")

        elif upstairs_options == "examine fireplace" and fireplace_lighted is True:
            slow_type("The fireplace is warm still, and the soot still reads: dtbcbv on the back wall.")

        elif upstairs_options == "use lighter" and "lighter" in inventory:
            lighter = input("What would you like to use it on?")
            if lighter == "fireplace":
                slow_type("""You reach into the arch of the fireplace with lighter in your hand. It takes a few tries 
but eventually the flame flickers to a start. You hold it to the kindling until it catches and relish in the warmth. You 
sit for a few minutes despite the urgency of your situation. 


You are about to get up and blow out the fire when you notice the soot gathering on the back wall of the fireplace, you
almost think nothing of it but you see letters start to form where the soot doesn't stick. 

dtbcbv

You wonder what that means as you stamp the fire out.""")
                fireplace_lighted = True

            elif lighter == "campfire":
                slow_type("You light the campfire it warms you for a minute before it goes out again.")
                campfire_lighted = True

            else:
                print("You can not use it on that.")

        elif upstairs_options == "use lighter" and "lighter" not in inventory:
            print("You do not have a lighter.")

        elif upstairs_options == "examine books" or upstairs_options == "examine bookshelf":
            slow_type("""The books and the shelves they are on are dusty. Books worn from age and spillages, stained 
pages make they words on the pages hard to read when you flip through it. You make out what you can:

The forest..... unsafe......monsters.... get out........stay away..... trees...... the lake....only......way......
...he'll find you. 


 You slam the book shut and shove it hastily back onto the shelf. You should leave.
 """)

        elif upstairs_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif upstairs_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif upstairs_options == "map" and got_map is True:
            print(player_map)  # displays the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif upstairs_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


# all scenes outside of the building that include the descriptions
def outside_1_scene():
    global got_map  # declares the map in the scene
    global player_health  # declares the player health variable in the scene

    # prints out a description based on the amount of health
    if enemy_1.health >= 1:

        print("")  # blank print for formatting
        slow_type(outside_1_description_with_enemy)  # displays the outside description with the enemy
        print("")  # blank print for formatting

    # prints out a description based on the amount of health
    elif enemy_1.health < 1:

        print("")  # blank print for formatting
        slow_type(outside_1_description_without_enemy)  # displays the outside description without the enemy
        print("")  # blank print for formatting

    else:
        print("I do not understand, type help for general instructions.")  # asking the player to reenter

    while True:

        print("")  # blank print for formatting
        outside_1_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if enemy_1.health >= 1:
            slow_type("""Before you can even attempt to move the monster bares it's yellowing fangs at you, deep
growl once again rattling through your body. Your eyes lock and you know that their is no escaping, you have to either 
fight it or die. 

You really don't want to die right now.""")

            while True:
                if enemy_1.health >= 1:

                    print("")
                    usr = input("What would you like to use: ")
                    print("")
                    usr_words = usr.split(" ")  # list
                    enemy_attack = random.randrange(1, 4)

                    for weapon in usr_words:
                        if weapon in inventory:
                            if weapon == "crowbar":
                                print("You lift the crowbar up and smack it down onto the ", enemy_1.name, ".")
                                enemy_1.health = enemy_1.health - weapon_damage["crowbar"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_1.attack
                                    print("The monster swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "knife":
                                print("You get close enough to drive your knife into it, it shrieks in pain.")
                                enemy_1.health = enemy_1.health - weapon_damage["knife"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_1.attack
                                    print("The monster swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "shovel":
                                print("You lift the shovel into the air and bring it down hard and fast.")
                                enemy_1.health = enemy_1.health - weapon_damage["shovel"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_1.attack
                                    print("The monster swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "ore":
                                print("You can tell the ore doesn't do much but all the damage you can get helps.")
                                enemy_1.health = enemy_1.health - weapon_damage["ore"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_1.attack
                                    print("The monster swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "bandages" and player_health < 150:
                                print("You pull the bandages out of you bag and carefully wrap your wounds.")
                                player_health = player_health + 50
                                if player_health > 150:
                                    player_health = 150
                                    print(player_health)
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "bandages" and player_health == 150:
                                print("You are not injured.")

                        elif usr == "inventory":  # if inventory is entered ut will carry out these functions:
                            print(inventory)  # displays the inventory guide

                        elif check is False:
                            print("You have no weapons, you flee before it can get you.")
                            outside_5_scene()

                        elif weapon not in inventory:
                            print("Please use a weapon you actually have.")

                        else:  # if no other option is fitting it will carry out these functions:
                            # asking the player to reenter
                            print("I do not understand, type help for general instructions.")

                elif enemy_1.health <= 0:
                    print("")
                    slow_type("""The monster collapses to the ground, an ear piercing screech echos around the trees.
They sway with the vibrations. You worry that the sound will alert anyone... or anything around that you are here. You
are glad that you survived.""")
                    break


                else:  # if no other option is fitting it will carry out these functions:
                    print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif outside_1_options == "north":  # if south is entered it will carry out these functions:
            outside_5_scene()

        elif outside_1_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_1_options == "south":  # if south is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_1_options == "west":  # if west is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif enemy_1.health < 1 and outside_1_options == "examine monster" and "steering wheel" not in inventory:
            slow_type("""Blood pours out of its mouth, eyes open and staring straight into your own. You still can't
tell quite what it is but monster fits it far too well. You are hesitant but still you want to be sure so you kick it 
gently, then slightly harder when it doesn't move. You hope you can go home soon. 

As you go to turn away from it something glints in the cracks of its skin.""")
            monster = input("Would you like to investigate? ")
            if monster == "yes":
                slow_type("""You reach towards the corpse of the monster, hands trembling. God, this is so gross but
it could be important so you suppose you'll have too. It squelches unpleasantly as your hand makes contact, it's fair 
wetter than you were expecting. After what feels like an entire lifetime but is barely 3 seconds your hand touches
something hard. You briefly consider it could be bone, or something like it but it's cold, metal maybe. Still, you yank
it out. Blood squirts across you as it does, it gets in your eye. 

When you manage to get the blood out you finally look at what's in you hand. A steering wheel. Huh. That's weird.

You tak it with you.""")
                inventory.append("steering wheel")

            elif monster == "no":
                slow_type("You leave it on the ground.")

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif enemy_1.health < 1 and outside_1_options == "examine monster" and "steering wheel" in inventory:
            slow_type("The monster remains on the ground where you left it.")

        elif outside_1_options == "examine path":
            slow_type("""The path was not made to be here. Years of people walking here over and over and over. There
are still footprints imprinted in the mud, someone has been coming here. You dread to think why. If someone came and 
saw the beast that lays dead but got away or if they've been here for something else... 

Perhaps they were feeding it...

...
""")

        elif outside_1_options == "examine trees" or outside_1_options == "examine tree":
            slow_type("""You aren't quite sure what time of day it is. Just that it's dark out but you fear the trees 
are making it worse. They loom over you, unnaturally tall. Maybe they were grown to hide the monster. Maybe theres just
something wrong with this place. An owl hoots from amongst the branches, a hiss slips into the sound and you fear that 
it's angry too.""")

        elif outside_1_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_1_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_1_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are on the thin path in the top left.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_1_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_2_shack_scene():
    global got_map  # declares the map in the scene

    print("")  # blank print for formatting
    slow_type(outside_2_shack_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_2_shack_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if outside_2_shack_options == "north":  # if south is entered it will carry out these functions:
            outside_6_crossroads_scene()

        elif outside_2_shack_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_2_shack_options == "south":  # if west is entered it will carry out these functions:
            upstairs_scene()  # lets the player know there is no path there

        elif outside_2_shack_options == "west":  # if south is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_2_shack_options == "examine shack" and "ore" not in inventory:
            slow_type("""The shack is badly put together, there are cracks and holes all over the mismatched wood. It's 
clear that the wear and tear over the years had gotten too much and the wood slats had been replaced one at a time when
needed. It's smaller than the basement, windows boarded up and glass missing. The roof looks like it could just slide 
off if a strong enough wind blows through. You are glad to have gotten out sooner rather than later. Leaning against the
shack is some type of wooden stick.""")
            ore_1 = input("Would you like to investigate further?")
            if ore_1 == "yes":
                slow_type("When you look closer you realise it's an ore.")
                take_ore = input("Would you like to take it with you?")
                if take_ore == "yes":
                    slow_type("You take the ore,  you have no idea how you're going to carry it but you will.")
                    inventory.append("ore")

                elif take_ore == "no":
                    slow_type("You leave it where it is")

                else:  # if no other option is fitting it will carry out these functions:
                    print("I do not understand, type help for general instructions.")  # asking the player to reenter

            elif ore_1 == "no":
                slow_type("The stick stays where it is.")

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif outside_2_shack_options == "examine shack" and "ore" in inventory:
            slow_type("""The shack is badly put together, there are cracks and holes all over the mismatched wood. It's 
clear that the wear and tear over the years had gotten too much and the wood slats had been replaced one at a time when
needed. It's smaller than the basement, windows boarded up and glass missing. The roof looks like it could just slide 
off if a strong enough wind blows through. You are glad to have gotten out sooner rather than later.""")

        elif outside_2_shack_options == "examine path":
            slow_type("""The path looks like most paths, the gravel crunches underneath your feet. You like the sound 
but it echos against the quiet of the woods. A cricket chirps. At least you aren't alone.""")

        elif outside_2_shack_options == "examine trees" or outside_2_shack_options == "examine tree":
            slow_type("""The trees loom over you, branches swaying against the wind, there is something off about them 
but you can't put your finger on it.""")

        elif outside_2_shack_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_2_shack_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_2_shack_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are outside the shack at the top of the map.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_2_shack_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_3_scene():
    global player_health  # declares the players health in the scene
    global got_map  # declares the map in the scene
    weapons_got = ["ore", "crowbar", "shovel", "knife"]

    # prints out a description based on the amount of health
    if enemy_2.health >= 1:

        print("")  # blank print for formatting
        slow_type(outside_3_description_with_enemy)  # displays the outside description with the enemy
        print("")  # blank print for formatting

    # prints out a description based on the amount of health
    elif enemy_2.health < 1:

        print("")  # blank print for formatting
        slow_type(outside_3_description_without_enemy)  # displays the outside description without the enemy
        print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_3_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if enemy_2.health >= 1:
            slow_type("""You try to move but the bugbear see you before you can. It roars as it's eyes track every move
you make. You don't really have a choice on what you have to do now... It's you or it, and you'd really rather it wasn't
you.""")

            while True:
                if enemy_2.health >= 1:

                    print("")
                    usr = input("What would you like to use: ")
                    print("")
                    usr_words = usr.split(" ")  # list
                    enemy_attack = random.randrange(1, 4)

                    for weapon in usr_words:
                        if weapon in inventory:
                            if weapon == "crowbar":
                                print("You lift the crowbar up and smack it down onto the ", enemy_2.name, ".")
                                enemy_2.health = enemy_2.health - weapon_damage["crowbar"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_2.attack
                                    print("The Bugbear swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "knife":
                                print("You get close enough to drive your knife into it, blood pours out of the cut.")
                                enemy_2.health = enemy_2.health - weapon_damage["knife"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_2.attack
                                    print("The Bugbear swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "shovel":
                                print("You heave the shovel up and bring it down onto it even faster.")
                                enemy_2.health = enemy_2.health - weapon_damage["shovel"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_2.attack
                                    print("The Bugbear swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "ore":
                                print("The ore does not do much damage")
                                enemy_2.health = enemy_2.health - weapon_damage["ore"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_2.attack
                                    print("The Bugbear swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "bandages" and player_health < 150:
                                print("You pull the bandages out of you bag and carefully wrap your wounds.")
                                player_health = player_health + 50
                                if player_health > 150:
                                    player_health = 150
                                    print(player_health)

                            elif weapon == "bandages" and player_health == 150:
                                print("You are not injured.")

                            else:  # if no other option is fitting it will carry out these functions:
                                # asking the player to reenter
                                print("Please use a weapon you have.")

                        elif check is False:
                            print("You have no weapons, you flee before it can get you.")
                            outside_7_t_junction_scene()

                        elif weapon not in inventory:
                            print("Please use a weapon you actually have.")

                        else:  # if no other option is fitting it will carry out these functions:
                            # asking the player to reenter
                            print("I do not understand, type help for general instructions.")

                elif enemy_2.health <= 0:
                    slow_type("""The monster collapses to the ground, an ear piercing screech echos around the trees.
They sway with the vibrations. You worry that the sound will alert anyone... or anything around that you are here. You
are glad that you survived.""")
                    break

                else:
                    print("")

        elif outside_3_options == "north":  # if south is entered it will carry out these functions:
            outside_7_t_junction_scene()

        elif outside_3_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_3_options == "south":  # if west is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        # if west is entered and the enemy has zero health it will carry out these functions:
        elif outside_3_options == "west" and enemy_2.health <= 0:
            outside_4_scene()

        elif enemy_2.health < 1 and outside_3_options == "examine bugbear":
            slow_type("""The bugbear is dead, thankfully. It looks just as intimidating as it did when it was alive. 
Except you aren't at as much risk of imminent death as you were before you killed it. You're glad. You hate this 
place with a passion. When you get out of here no ones ever going to believe you beat this thing... Or that it was real
in the first place.""")

        elif outside_3_options == "examine path":
            slow_type("The path is muddy and gross. You leave footprints with every step you take.")

        elif outside_3_options == "examine trees" or outside_3_options == "examine tree" and "drink" not in inventory:
            slow_type("""You didn't realise trees could be creepy. Yet here they are anyway. Looming over you 
unnaturally. You wish someone would cut them all down. There something hidden amongst the moss at the bottom.""")

            drink = input("Would you like to investigate further?")
            if drink == "yes":
                slow_type("You look closer you and find it's a bottle of water.")
                take_drink = input("Would you like to take it with you?")
                if take_drink == "yes":
                    slow_type("You shove it into you pocket.")
                    inventory.append("water")

                elif take_drink == "no":
                    slow_type("You leave it where it is.")

                else:  # if no other option is fitting it will carry out these functions:
                    print("I do not understand, type help for general instructions.")  # asking the player to reenter

            elif drink == "no":
                slow_type("The drink stays where it is.")

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif outside_3_options == "examine trees" or outside_3_options == "examine tree" and "drink" in inventory:
            slow_type("""You didn't realise trees could be creepy. Yet here they are anyway. Looming over you 
unnaturally. You wish someone would cut them all down.""")

        elif outside_3_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_3_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_3_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are on the thin split path in the top right.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_3_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_4_scene():
    global got_map  # declares the map in the scene

    print("")  # blank print for formatting
    slow_type(outside_4_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_4_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if outside_4_options == "north":  # if south is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_4_options == "east":  # if east is entered it will carry out these functions:
            outside_3_scene()

        elif outside_4_options == "south":  # if south is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_4_options == "west":  # if west is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_4_options == "examine outhouse" and "petrol" not in inventory:
            slow_type("""The outhouse is small, you can fit in but its a tight squeeze. The door doesn't move from its
place even if you try and force it. You don't know how it's staying so still considering how little of it is actually 
attached to anything. There something shinning in the toilet, you dread to think what it could be and why it would be 
kept here of all places.""")
            outhouse = input("Would you like to investigate? ")
            if outhouse == "yes":
                slow_type("""Out all the things you thought you would spend your day doing after being kidnapped, 
putting your hand down a obviously well used toilet in an outhouse in the middle of nowhere was not it. Yet here you are
It's uncomfortably wet, you're scared to know what it is but considering where your hand is you don't really need to 
guess. When your hand wraps around something metal and cold you pull it out, shake your hand off, then question who the
thought putting a canister of petrol in the toilet was a good idea? At least you have it now.""")
                inventory.append("petrol")

            elif outhouse == "no":
                slow_type("You leave it where it is.")

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif outside_4_options == "examine outhouse" and "petrol" in inventory:

            slow_type("""The outhouse is small, you can fit in but its a tight squeeze. The door doesn't move from its
place even if you try and force it. You don't know how it's staying so still considering how little of it is actually 
attached to anything.""")

        elif outside_4_options == "examine path":
            slow_type("The path is just as muddy and gross as the rest. Your shoes are never going to be the same.")

        elif outside_4_options == "examine trees" or outside_4_options == "examine tree":
            slow_type("You're beginning to hate the sight of these trees. They all look the same.")

        elif outside_4_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_4_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_4_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are on the thin road in the top right.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_4_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_5_scene():
    global got_map  # declares the map in the scene
    global player_health

    print("")  # blank print for formatting
    slow_type(outside_5_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_5_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if outside_5_options == "north":  # if south is entered it will carry out these functions:
            outside_9_building_scene()

        elif outside_5_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_5_options == "south":  # if south is entered it will carry out these functions:
            outside_1_scene()

        elif outside_5_options == "west":  # if west is entered it will carry out these functions:
            outside_6_crossroads_scene()

        elif outside_5_options == "examine bushes" or outside_5_options == "examine bush":
            slow_type("""The bush is small, leaves mainly green with yellowing edges. There is a weird gap within the
leaves. You lean towards it. You still can't tell what it is.""")
            knife = input("Would you like to investigate further?")
            if knife == "yes":
                slow_type("You stick your hand in and find it's a knife, it cuts your hand.")
                player_health = player_health - 5
                take_knife = input("Would you like to take it with you?")
                if take_knife == "yes":
                    slow_type("You carefully place it into you pocket.")
                    inventory.append("knife")

                elif take_knife == "no":
                    slow_type("The knife stays where it is.")

                else:  # if no other option is fitting it will carry out these functions:
                    print("I do not understand, type help for general instructions.")  # asking the player to reenter

            elif knife == "no":
                slow_type("The knife stays where it is.")

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif outside_5_options == "examine path":
            slow_type("""The main path is gravel, rocks crunching underneath your feet as you walk. There dirt path 
that comes off it has some of the stones scatter within it. A pretty standard path if you were asked.""")

        elif outside_5_options == "trees" or outside_5_options == "examine tree":
            slow_type("The trees continue to be the same as all the other trees you've seen.")

        elif outside_5_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_5_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_5_options == "map" and got_map is True:
            print(player_map)  # displays the map
            # where the player is on the map
            print("You are at the bend in the path on the left with the thin road going up.")

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_5_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_6_crossroads_scene():
    global got_map  # declares the map in the scene
    global glove_box_opened  # declares the glove box opened variable in scene.

    print("")  # blank print for formatting
    slow_type(outside_6_crossroads_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_6_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if outside_6_options == "north":  # if north is entered it will carry out these functions:
            outside_10_scene()

        elif outside_6_options == "east":  # if east is entered it will carry out these functions:
            outside_5_scene()

        elif outside_6_options == "south":  # if south is entered it will carry out these functions:
            outside_2_shack_scene()

        elif outside_6_options == "west":  # if west is entered it will carry out these functions:
            outside_7_t_junction_scene()

        elif outside_6_options == "examine sign" or outside_6_options == "examine signpost":
            slow_type("""The sign post is pretty much laying flat on the floor, yet the part of it still in the ground
is keeping it a few centimeters of the ground. At the top there use to be four arrows point in each directions but you 
can only see three... well two and a half since one has the end snapped off. The wood for them is rotted, only a few 
letters stick out on each one. Looking around you see what might be the other one in the bush over the other side of the 
of the path. The pole is rusted and covered in overgrown plants.""")

        elif outside_6_options == "examine bush":
            slow_type("""The bush is like any other bush, except the wooden sign half stuck out of it. You reach in, 
thorns pricking your skin as you do, and pull the sign out. It's not as ruined as the others, the words underneath are 
covered by what you hope is red paint. The 'paint' reads: \033[1;31mGET OUT\033[0;39m \n but the words it covers say: 
Lake Nene. You put the sign back in the bush. You should get out of here.""")

        elif outside_6_options == "examine car":
            slow_type("""The front of the car is wrapped around the signpost and the back looks as though another car
had driven at high speeds into it. The door sticks as you try to open it. While it takes a little force you are able to 
get in, the door creaks as in its place as you slide into the front seat. You can't get into the backseat, but from what
you can tell it was empty anyway except a few stray wrappers. The front seems mostly fine, glass litters the seats from
the front windshield. The steering wheel is missing, though the car couldn't drive anyway. The glove box is closed and 
the radio is off. There are CDs in the door pockets, whoever owns this car has terrible taste.""")

            while True:
                print("")  # blank print for formatting
                car_options = input("what would you like to do? ").lower()  # gets the players input
                print("")  # blank print for formatting

                if car_options == "exit car":
                    slow_type("You force the door back open and step out of the car.")
                    break

                elif car_options == "examine glovebox" or car_options == "examine glove box":
                    if glove_box_opened is False:
                        slow_type("""The glove box is a pretty standard glove box and is in pretty good condition 
considering how the rest of the car looks.""")

                    elif glove_box_opened is True:
                        slow_type("The glove box is the same as it was last time.")

                    else:
                        print("")

                elif car_options == "open glovebox" or car_options == "open glove box":
                    if glove_box_opened is False:
                        slow_type("""The glove box clicks open, CDs fall out. Clattering onto the ground before you can 
stop them. You push everything in there around, you think there is nothing of note in there at first but eventually you
find a lighter hidden in the back. You grab it, slide it into your pocket. You go to close the glove box and decide last 
second to put all the CDs back in.""")
                        inventory.append("lighter")
                        glove_box_opened = True

                    elif glove_box_opened is True:
                        slow_type("""You open the glove box, once again all the CDs fall out onto the ground. You sigh. 
Typical. There's nothing new since the last time you checked, that would be worrying, so you force all the CDs back in 
and slam it shut.""")

                    else:
                        print("")

                else:  # if no other option is fitting it will carry out these functions:
                    # asking the player to reenter
                    print("I do not understand, type help for general instructions. Perhaps try 'exit car'.")

        elif outside_6_options == "examine tree" or outside_6_options == "examine trees":
            slow_type("""The trees are tall, taller than you think is normal. You don't know what type of tree they are
and to be honest you don't care. Trees, no matter how creepy they may or may not be, are the least of your problems 
right now.""")

        elif outside_6_options == "examine path":
            slow_type("""It's like most gravel paths you've seen in your life. Though this one is a crossroads so at 
least that's different. You read an mythology book once that you can summon a crossroad demon that will give you what
ever you want in exchange for your soul here. You consider it briefly. You don't have a photo of yourself and you're 
pretty sure that was important to the summoning.""")

        elif outside_6_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_6_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_6_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are at the crossroads.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_6_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_7_t_junction_scene():
    global got_map  # declares the map in the scene

    print("")  # blank print for formatting
    slow_type(outside_7_T_junction_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_7_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if outside_7_options == "north":  # if south is entered it will carry out these functions:
            outside_11_scene()

        elif outside_7_options == "east":  # if east is entered it will carry out these functions:
            outside_6_crossroads_scene()

        elif outside_7_options == "south":  # if west is entered it will carry out these functions:
            outside_3_scene()

        elif outside_7_options == "west":  # if south is entered it will carry out these functions:
            outside_8_graveyard_scene()

        elif outside_7_options == "examine tree" or outside_7_options == "examine trees":
            slow_type("""Considering how little there is at this T-junction, the fact that you were surprised at how 
similar the tree here are compared to everywhere else, was surprising in and of itself.""")

        elif outside_7_options == "examine path":
            slow_type("""The path is gravel, like everywhere else has been too. It's in a T shape though you don't know 
any demon summoning rituals for this one. There is a dirt path going off the T so one could argue this is a crossroads 
too, you would be able to do the same ritual then.""")

        elif outside_7_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_7_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide
            # if map is entered and the player has the map it will carry out these functions:

        elif outside_7_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are at the T junction with the thin path going up.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_7_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_8_graveyard_scene():
    global got_map  # declares the map in the scene
    global grave_dug

    print("")  # blank print for formatting
    slow_type(outside_8_graveyard_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_8_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if outside_8_options == "north":  # if north is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_8_options == "east":  # if east is entered it will carry out these functions:
            outside_7_t_junction_scene()

        elif outside_8_options == "south":  # if south is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_8_options == "west":  # if west is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_8_options == "examine headstone" or outside_8_options == "examine headstones":
            slow_type("""The headstones have all been hand carved. All names of people you don't know. You thought this
might be a family grave yard but none of the names match. All the graves look pretty similar, well looked after similar
to the basement and so unlike the shack above. The last grave is nameless though the tools to carve it sit next to the
headstone.""")

        elif outside_8_options == "examine graves" or outside_8_options == "examine grave":
            slow_type("""Like the headstone the graves are in excellent condition, each grave it made of straight lines.
like someone took the time to perfectly measure each one before digging. It seems like a lot of effort.""")

        elif outside_8_options == "examine nameless grave":
            slow_type("""If you had to guess you recon you would fit in the hole dug perfectly. It sends a shiver 
straight down your spine. The carving tools next to the headstone look perfectly looked after. None of this feels right
to you.""")

        elif outside_8_options == "examine path":
            slow_type("""The path tapers off well before you get to the grave, though a stone from it had been stuck in 
your shoe for a while now so it's never really gone.""")

        elif outside_8_options == "examine trees" or outside_8_options == "examine tree":
            slow_type("""Trees that are too tall and too wide and far too intimidating for what they are loom over you.
it casts a shadow over the graves and makes the whole area scarier than it should be.""")

        elif outside_8_options == "use shovel":
            shovel = input("What would you like to use the shovel on? ")
            if shovel == "grave" or shovel == "graves" and grave_dug is False:
                slow_type("""You dig the shovel into the ground and throw the pile behind you. Wow, this is going to be
a piece of cake.

...

...

By the time you hit anything you are panting and sweating and just all around having a terrible time. You didn't think
it would be this hard. Next time you need to dig up a grave, consider not doing that. Still, you finally hit something 
and it doesn't take much longer before you're able to get it out of the ground. It's heavy and makes your muscles ache
even more. A motor. Yay.""")
                inventory.append("motor")
                grave_dug = True

            elif shovel == "grave" or shovel == "graves" and grave_dug is True:
                slow_type("The grave has already been dug, you could dig further put there isn't much point.")

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif outside_8_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_8_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_8_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are on the path on the right side of the map.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_8_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_9_building_scene():
    global got_map  # declares the map in the scene

    print("")  # blank print for formatting
    slow_type(outside_9_building_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_9_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if outside_9_options == "north":  # if south is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_9_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_9_options == "south":  # if south is entered it will carry out these functions:
            outside_5_scene()

        elif outside_9_options == "west":  # if west is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        # if examine shovel is entered it will carry out these functions:
        elif outside_9_options == "examine shovel" and "shovel" not in inventory:
            slow_type("The shovel is somewhat new. It has definitely been used. ")  # displays the description
            shovel = input("Would you like to take it with you? ")  # gets the players input
            if shovel == "yes":  # if yes is entered it will carry out these functions:
                inventory.append("shovel")  # adds crowbar to inventory

            elif shovel == "no":  # if no is entered it will carry out these functions:
                slow_type("You drop the shovel back onto the ground.")  # displays the description

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        # if examine shovel is entered it will carry out these functions:
        elif outside_9_options == "examine shovel" and "shovel" in inventory:
            slow_type("You already took the shovel.")  # displays the description

        elif outside_9_options == "examine building":
            slow_type("""""")

        elif outside_9_options == "examine door":
            slow_type("""""")

        elif outside_9_options == "examine path":
            slow_type("""""")

        elif outside_9_options == "examine tree" or outside_9_options == "examine trees":
            slow_type("""""")  
            
        elif outside_9_options == "use flashlight":
            slow_type("""""")
            
        elif outside_9_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_9_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_9_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are at the building at the bottom left.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_9_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_10_scene():
    global got_map  # declares the map in the scene

    print("")  # blank print for formatting
    slow_type(outside_10_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_10_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if outside_10_options == "north":  # if north is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_10_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_10_options == "south":  # if south is entered it will carry out these functions:
            outside_6_crossroads_scene()

        elif outside_10_options == "west":  # if west is entered it will carry out these functions:
            outside_11_scene()
            
        elif outside_10_options == "examine path":
            slow_type("""""")

        elif outside_10_options == "examine tree" or outside_10_options == "examine trees":
            slow_type("""""")  
            
       
        elif outside_10_options == "examine bush" or outside_10_options == "examine bushes":
            slow_type("""""")
            
         elif outside_10_options == "examine plank" or outside_10_options == "examine planks" and "ore 2" not in inventory:
            slow_type("""""")
            ore_2 = input("Would you like to investigate further?")
            if ore_2 == "yes":
                slow_type("When you look closer you realise it's an ore.")
                take_ore = input("Would you like to take it with you?")
                if take_ore == "yes":
                    slow_type("You take the ore, you have no idea how you're going to carry it but you will.")
                    inventory.append("ore")

                elif take_ore == "no":
                    slow_type("You leave it where it is")

                else:  # if no other option is fitting it will carry out these functions:
                    print("I do not understand, type help for general instructions.")  # asking the player to reenter

            elif ore_1 == "no":
                slow_type("The stick stays where it is.")

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif outside_10_options == "examine plank" or outside_10_options == "examine planks" and "ore 2" in inventory:
            slow_type("""""")
            
        elif outside_9_options == "examine stinging nettles":
            slow_type("""""")     
       
        elif outside_10_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_10_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_10_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are in the left curve of the split path.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_10_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_11_scene():
    global got_map  # declares the map in the scene

    print("")  # blank print for formatting
    slow_type(outside_11_split_path_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_11_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if outside_11_options == "north":  # if south is entered it will carry out these functions:
            lake_scene()

        elif outside_11_options == "east":  # if east is entered it will carry out these functions:
            outside_10_scene()

        elif outside_11_options == "south":  # if west is entered it will carry out these functions:
            outside_7_t_junction_scene()

        elif outside_11_options == "west":  # if south is entered it will carry out these functions:
            outside_12_scene()

        elif outside_11_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide
            
        elif outside_11_options == "examine path":
            slow_type("""""")

        elif outside_11_options == "examine tree" or outside_11_options == "examine trees":
            slow_type("""""")  
            
        elif outside_11_options == "examine bush" or outside_11_options == "examine bushes":
            slow_type("""""")

        elif outside_11_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_11_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are on the split path.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_11_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def outside_12_scene():
    global got_map  # declares the map in the scene
    global player_health  # declares the player health variable in the scene

    # prints out a description based on the amount of health
    if enemy_3.health >= 1:

        print("")  # blank print for formatting
        slow_type(outside_12_description_with_enemy)  # displays the outside description with the enemy
        print("")  # blank print for formatting

    # prints out a description based on the amount of health
    elif enemy_3.health < 1:

        print("")  # blank print for formatting
        slow_type(outside_12_description_without_enemy)  # displays the outside description without the enemy
        print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        outside_12_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if enemy_3.health >= 1:
            slow_type("""The Karkinos snaps it claws angrily when you attempt to move, you know that you really don't 
have much of a choice and you will have to fight it one way or another. It might have 4 more legs than you but you are 
sure you can survive.

Hopefully.
""")

            while True:
                if enemy_3.health >= 1:

                    print("")
                    usr = input("What would you like to use: ")
                    print("")
                    usr_words = usr.split(" ")  # list
                    enemy_attack = random.randrange(1, 4)
                    for weapon in usr_words:
                        if weapon in inventory:
                            if weapon == "crowbar":
                                print("You swing the crowbar in the Karkinos, it howls in pain.")
                                enemy_3.health = enemy_3.health - weapon_damage["crowbar"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_3.attack
                                    print("The Karkinos swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "knife":
                                print("You get close enough to drive your knife into it, it swings it claws aimlessly.")
                                enemy_3.health = enemy_3.health - weapon_damage["knife"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_3.attack
                                    print("The Karkinos swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "shovel":
                                print("You lift the shovel into the air and bring it down hard and fast.")
                                enemy_3.health = enemy_3.health - weapon_damage["shovel"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_3.attack
                                    print("The Karkinos swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "ore":
                                print("The ore doesn't hurt it much but the creature hisses in pain anyway.")
                                enemy_3.health = enemy_3.health - weapon_damage["ore"]
                                if enemy_attack == 3:
                                    player_health = player_health - enemy_3.attack
                                    print("The Karkinos swings back at you. You have ", player_health, " health.")
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "bandages" and player_health < 150:
                                print("You pull the bandages out of you bag and carefully wrap your wounds.")
                                player_health = player_health + 50
                                if player_health > 150:
                                    player_health = 150
                                    print(player_health)
                                    if player_health <= 0:
                                        print("You collapse to the ground, you were so close.")
                                        quit()

                            elif weapon == "bandages" and player_health == 150:
                                print("You are not injured.")

                        elif usr == "inventory":  # if inventory is entered ut will carry out these functions:
                            print(inventory)  # displays the inventory guide

                        elif check is False:
                            print("You have no weapons, you flee before it can get you.")
                            outside_12_scene()

                        elif weapon not in inventory:
                            print("Please use a weapon you actually have.")

                        else:  # if no other option is fitting it will carry out these functions:
                            # asking the player to reenter
                            print("I do not understand, type help for general instructions.")

                elif enemy_3.health <= 0:
                    slow_type("""The monster collapses to the ground, an ear piercing screech echos around the trees.
They sway with the vibrations. You worry that the sound will alert anyone... or anything around that you are here. You
are glad that you survived.""")
                    break

                else:
                    print("")

        elif outside_12_options == "north":  # if south is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_12_options == "east":  # if east is entered it will carry out these functions:
            outside_11_scene()

        elif outside_12_options == "south":  # if south is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif outside_12_options == "west":  # if west is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way
            
        elif outside_12_options == "examine path":
            slow_type("""""")

        elif outside_12_options == "examine tree" or outside_10_options == "examine trees":
            slow_type("""""")  
            
        elif enemy_3.health < 1 and outside_12_options == "examine karkinos":
            slow_type("""""")

        elif outside_12_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif outside_12_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif outside_12_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are on the thin path at the bottom right")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif outside_12_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def lake_scene():
    global got_map  # declares the map in the scene
    global boat_unlocked
    global boat_code
    global obtained_items

    print("")  # blank print for formatting
    slow_type(lake_description)  # displays the outside description
    print("")  # blank print for formatting

    while True:

        print("")  # blank print for formatting
        lake_options = input("what would you like to do? ").lower()  # gets the players input
        print("")  # blank print for formatting

        if lake_options == "north":  # if south is entered it will carry out these functions:
            print("There is a lake, you are unable to go that way without a boat.")

        elif lake_options == "east":  # if east is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif lake_options == "south":  # if south is entered it will carry out these functions:
            outside_11_scene()

        elif lake_options == "west":  # if west is entered it will carry out these functions:
            print("You cannot go that way, you will get lost in the woods.")  # tells the player they can't go that way

        elif lake_options == "examine path":
            slow_type("""The gravel path tapers out as it gets closer to the lake, eventually it starts to blend into the
sand of the beach. You hate sand. it's never going to get out of your shoes.""")

        elif lake_options == "examine trees" or lake_options == "examine tree":
            slow_type("The trees are no different to the rest of the trees you've seen today. It's nice and creepy.")

        elif lake_options == "examine lake":
            slow_type("""The lake spreads out far and wide, going almost further than you can see. There's more land
just inside of your eye line. A light flashes. Right. You just have to cross this lake and you're out of here. You can't 
quite see the bottom even a meter out. It's going to be fine, it's not even that bad...""")

        elif lake_options == "examine rubbish":
            slow_type("""The rubbish is kind of gross, the smell alone is off putting. You would normally be upset at 
someone littering but at the moment you have bigger issues to deal with considering your recent kidnapping.""")

        # the boat needs to be unlocked and have all of the parts to work
        elif lake_options == "examine boat" and boat_unlocked is False:
            slow_type("""The boat is... not great. You definitely think it could work to get it out of here, you don't 
really have much of a choice otherwise. The boat is chained to a tree going through both the door to get in and some 
rod sticking out the side. A code base padlock keeping it in place. You'll have to find that code if you want any chance 
of getting out of here. You try to get a better look through one of the windows to the cabin, you think some parts might
be missing... Great... You'll have to find those too. 
""")
            print("")
            boat_option = input("Would you like to attempt to unlock the boat? ")
            if boat_option == "yes":
                print("")
                password = input("Please enter that password here: ")
                if password == boat_code:
                    slow_type("You type in the code and the lock clicks open. Hell yeah.")
                    boat_unlocked = True

                else:
                    print("That is incorrect.")

            elif boat_option == "no":
                slow_type("The boat stays locked.")

            else:  # if no other option is fitting it will carry out these functions:
                print("I do not understand, type help for general instructions.")  # asking the player to reenter

        elif lake_options == "enter boat" and boat_unlocked is True:
            if "motor" and "steering wheel" and "petrol" in inventory:
                slow_type("""You click the steering wheel into place, plug the motor in, fill the petrol tank. You 
aren't sure it's all been done right but it's all you've got at the moment. You really, really want to get out of here. 
Away from the basement, away from the monsters, away from the creepy trees and the creepy owls back to your house with
your cat and your own bed.""")
                print("")
                final_option = input("Would you like to leave? ")
                if final_option == "yes":
                    ending()

            else:
                slow_type("""Now that the door is unlocked you are able to get inside the cabin, it's easier to tell 
whats missing now, the steering wheel is no where to be seen. The petrol gage is a millimeter off of empty and will 
barely get you off of the beach let alone somewhere with other people. The key is in the ignition, small mercies and all 
that, but you turn it and nothing happens. You go to check if everything is fine with the motor, it takes longer than 
you would hope but you've never been on a boat before and you find... nothing. It's gone. That's... fine. You will find 
everything you need and it'll be fine. 

You're sure that someone would just leave those things lying around...""")

            print("")

        elif lake_options == "help":  # if help is entered it will carry out these functions:
            print(help_guide)  # displays help guide

        elif lake_options == "inventory":  # if inventory is entered ut will carry out these functions:
            print(inventory)  # displays the inventory guide

        # if map is entered and the player has the map it will carry out these functions:
        elif lake_options == "map" and got_map is True:
            print(player_map)  # displays the map
            print("You are at the lake at the bottom.")  # where the player is on the map

        # if map is entered and the player doesn't have the map it will carry out these functions:
        elif lake_options == "map" and got_map is False:
            print("You do not have a map.")  # does not display the map

        else:  # if no other option is fitting it will carry out these functions:
            print("I do not understand, type help for general instructions.")  # asking the player to reenter


def ending():
    print("")


print("")  # blank print for formatting
slow_type(opening_text)  # displays the opening text which is defined earlier
starting_room_scene()  # starts the starting scene
