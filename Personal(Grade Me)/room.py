# Implement a class to hold room information. This should have name and
# description attributes.

class Room:


    def __init__(self, area, description, items=[]):
        self.area = area
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
        

    def __str__(self):
        return_string = "---------"
        return_string += "\n\n"
        return_string += f"***  {self.area}  ***"
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n\n"
        return_string += "---------"
        return return_string


    def print_valid_directions(self):
        return_string = "\nyou may travel: "
        return_string += f"{self.get_exits_string()}"
        return print(return_string)


    def room_item_keys(self):
        item_keys = []
        for x, y in self.items:
            item_keys.append(x)
        return item_keys


    def get_exits_string(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits