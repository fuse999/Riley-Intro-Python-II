# Write a class to hold player information, e.g. what room they are in
# currently.
import time

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.hit_points = 100


    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print("Can't go that way silly")
    

    def inventory_name(self):
        inventory_item_names = []
        for x, y in self.inventory:
            inventory_item_names.append(x)
        return inventory_item_names


    def print_inventory(self):
        inventory_item_names = []
        print(f"{self.name} is holding: ")
        for x, y in self.inventory:
            print(x)


    def eat(self, food_item):
        if not isinstance(food_item, Food):
            print(f"You cannot eat {food_item.name}")
        else:
            self.strength += food_item.calories
            print(f"You have eaten {food_item.name}, your strength is now {self.strength}")
            self.inventory.remove(food_item)


# logic: pick up object, and remove from room at same time.


    def pick_up(self, item_name):
        if item_name in self.current_room.room_item_keys():
            search = item_name
            for sublist in self.current_room.items:
                if sublist[0] == search:
                    self.inventory.append(sublist)
                    self.current_room.items.remove(sublist)
                break
        else:
            print(f"{item_name} is not here")
            time.sleep(1)


    def drop_item(self, item_name):
        if item_name in self.inventory_name():
            search = item_name
            for sublist in self.inventory:
                if sublist[0] == search:
                    self.current_room.items.append(sublist)
                    self.inventory.remove(sublist)
                break
        else:
            print(f"{item_name} is not in you inventory to drop")
            time.sleep(1)
            print("You Have Nothing MORTAL!!!")
            time.sleep(1)
