import time
from room import Room
from player import Player
from item import Item, Food, Egg, Ramen

rock = Item("rock", "This is a rock.")
egg = Food("egg", "This is an egg", 20)
sandwich = Food("sandwich", "This is a delicious sandwich.", 100)
ramen = Food("ramen", "Delicious - and easy to make!", 25)


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [["rock", rock], ["egg", egg]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [["sandwich", sandwich], ["ramen", ramen]]),

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

# Link rooms with item (Improve with dict name:lst_of_items)
room['outside'].rock = Item("rock", "This is a rock.")
room['outside'].egg = Food("egg", "This is an egg", 20)
room['foyer'].sandwich = Food("sandwich", "This is a delicious sandwich.", 100)
room['foyer'].ramen = Food("ramen", "Delicious - and easy to make!", 25)


# Main


# Make a new player object that is currently in the 'outside' room.
user = Player(input("What is your name, brave soul : "), room['outside'])
# user = Player("riley", room['outside'])
time.sleep(2)
print("---------")
print("\n\nStory yet to be written\n\n")
# print("---------")
time.sleep(1)
print(user.current_room)
time.sleep(1)

while True:
    print("\n")
    print("Possible commands: look around, walk, inventory, pick up, drop item, eat, quit")
    cmd = input("Enter Comand --> ")
    valid_actions = ("p", "d", "u")

    if cmd in ["quit", "q"]:
        print("Thank you for playing! Good Bye!")
        exit(0)

    elif cmd in ["walk", "w"]:
        user.current_room.print_valid_directions()
        cmd = input("\nIn which direction ~~> ")

        if cmd in user.current_room.get_exits_string():
            user.travel(cmd)
            time.sleep(1)
            print(user.current_room)
            time.sleep(1)

        else:
            # Print an error message if the movement isn't allowed.
            print("Not a valid move. Please enter: n, s, e, or w")

    elif cmd in ["inventory", "i"]:
        user.print_inventory()
        time.sleep(2)

    elif cmd in ["look around", "l"]:
        print(user.current_room)
        time.sleep(1)
        if user.current_room.room_item_keys() != []:
            print(f"Also You see {user.current_room.room_item_keys()} near you")
            print("---------")
        else:
            print("You see no items of importance")
            print("---------")

    elif cmd in ["pick up", "p"]:
        print(f"Also you can see {user.current_room.room_item_keys()} near you")
        cmd = input("What would you like to pick up: ")
        user.pick_up(cmd)
        print("\n")
        user.print_inventory()

    elif cmd in ["drop item", "d"]:
        user.print_inventory()
        cmd = input("What would you like to drop: ")
        user.drop_item(cmd)
        print(f"you have droped {cmd}")
        


    elif cmd in ["eat", "e"]:
        print("I don't feel hungry")
        # if user.inventory_name() != []:
        #     user.print_inventory()
        #     cmd = input("What would you like to eat: ")

        #     if cmd in user.inventory_name() and ["egg", "sandwich", "ramen"]:
        #         user.drop_item(cmd)
        #         user.print_inventory()

        #     else:
        #         print(f"You can only drop {user.inventory_name()}")

        # else:
        #     time.sleep(1)
        #     print("You Have Nothing MORTAL!!!")
        #     time.sleep(1)

    else:
        # Print an error message if the movement isn't allowed.
        print("Comand not a valid.\nPlease enter: walk, inventory, pick up, drop item, eat, or quit")
