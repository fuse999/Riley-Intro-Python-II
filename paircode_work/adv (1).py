from room import Room
from player import Player
from item import Item, Food, Egg, Ramen

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["rock", "egg"]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["sandwich", "ramen"]),
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

# Link rooms with item
room['outside'].rock = Item("rock", "This is a rock.")
room['outside'].egg = Egg()
room['foyer'].sandwich = Food("sandwich", "This is a delicious sandwich.", 100)
room['foyer'].ramen = Ramen()


# Main
#
# Make a new player object that is currently in the 'outside' room.

player = Player(input("Please enter your name: "), room['outside'])
# player.inventory.append(rock)
# player.inventory.append(sandwich)
# player.inventory.append(egg)
# player.inventory.append(ramen)
print(player.current_room)
Player.print_inventory(player)
# player.eat(rock)
# player.eat(sandwich)
# player.eat(egg)
# player.eat(ramen)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
valid_directions = ("n", "s", "e", "w")
while True:
    cmd = input("\n~~> ")
    if cmd == "q":
        print("Goodbye!")
        exit(0)
    elif cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "i":
        player.print_inventory()
    elif cmd == "p":
        print(f"You see {player.current_room.items} near you")
        cmd = input("What would you like to pick up: ")
        if cmd in player.current_room.items:
            Player.pick_up(player, cmd)
            Player.print_inventory(player)
        else:
            print(f"You can only pick up {player.current_room.items}")
    elif cmd == "d":
        print(Player.print_inventory(player))
        cmd = input("What would you like to drop: ")
        if cmd in Player.inventory_name(player):
            Player.drop_item(player, cmd)
            Player.print_inventory(player)
        else:
            print(f"You can only drop {Player.inventory_name(player)}")
        
        
    else:
        print("I did not understand that command\n")
        print(f"you can travel with {valid_directions}\n")
        print(f"Pick up items in room with p\n")
        print((f"Drop items with d"))