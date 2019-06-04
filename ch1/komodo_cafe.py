# Komodo Cafe Menu

class MenuItem:
    def __init__(self, name, number, description, ingredients, price):
        self.name = name
        self.number = number
        self.description = description
        self.ingredients = ingredients
        self.price = price
    
    def __repr__(self):
        return f"\n{self.name} is number {self.number}, costs ${self.price};\ncontains {self.ingredients}.\n{self.description}"
        # Format
            # Burger is number 1, costs $5; contains beef, cheese, and bread.
            # Very tasty.
    
class MenuRepository:
    def __init__(self):
        self.menu_list = []
        self.menu_number = 0

    def create_menu_item(self, name, number, description, ingredients, price):
        new_item = MenuItem(name, number, description, ingredients, price)
        self.menu_list.append(new_item)

    def get_menu_list(self):
        return self.menu_list

    def id_plus(self):
        self.menu_number += 1
        