from item import Food, Egg, Ramen

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.strength = 100


    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("You cannot move in that direction")
    def inventory_name(self):
        inventory_item_names = []
        # print("You are holding: ")
        for item in self.inventory:
            inventory_item_names.append(item.name)
            # print(item.name)
        return inventory_item_names


    def print_inventory(self):
        inventory_item_names = []
        print("You are holding: ")
        for item in self.inventory:
            print(item.name)

    def eat(self, food_item):
        if not isinstance(food_item, Food):
            print(f"You cannot eat {food_item.name}")
        else:
            self.strength += food_item.calories
            print(f"You have eaten {food_item.name}, your strength is now {self.strength}")
            self.inventory.remove(food_item)

# logic: pick up object, and remove from room at same time.

    def pick_up(self, item_name):
        self.inventory.append(getattr(self.current_room, item_name))
        self.current_room.items.remove(item_name)


    def drop_item(self, item_name):
        self.inventory.remove(getattr(self.current_room, item_name))
        self.current_room.items.append(item_name)
