import time
from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name, brave soul : "), room['outside'])
# player = input("What is your name, brave soul : "), room['outside']
# print(player)
# Write a loop that:
# player_cmd = ""
# while player_cmd not in ():
while True:
    # * Prints the current room name
    time.sleep(1)
    current_room = player.current_room
    print(f"location:  *** {current_room.area} ***")
    time.sleep(2)
# * Prints the current description (the textwrap module might be useful here).
    print(f"*** {current_room.description} ***")
    time.sleep(2.5)
# * Waits for user input and decides what to do.
    move = input("Enter The Direction you would like to travel : ")
    if move == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
        else:
            print("Can't go that way silly")
    elif move == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
        else:
            print("Can't go that way silly")
    elif move == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
        else:
            print("Can't go that way silly")
    elif move == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
        else:
            print("Can't go that way silly")
        # If the user enters "q", quit the game.
    elif move == "q":
        print("Thank you for playing! Good Bye!")
        exit()
    else:
        # Print an error message if the movement isn't allowed.
        print("Not a valid move. Please enter: n, s, e, w or q")