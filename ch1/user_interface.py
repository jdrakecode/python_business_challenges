# Interface for Komodo Cafe Menu
from komodo_cafe import MenuRepository

class MainMenu:
    def __init__(self):
        self.menu_repo = MenuRepository()
        self.choice = {
            "1": self.create_item,
            "2": self.delete_item,
            "3": self.list_items,
            "4": exit
        }
    
    def display_menu(self):
        print(
"""
What would you like to do?:
1. Create menu item
2. Delete menu item
3. List all menu items
4. Exit
"""
        )
    
    def create_item(self):
        name = input("Name of item?\n> ") # user's input assigned to var
        self.menu_repo.id_plus() # THIS TOOK ME 3 HOURS TO FIGURE OUT / increments id by 1
        number = self.menu_repo.menu_number # assigns id
        description = input("Enter a description:\n> ")
        ingredients = input("Ingredients?\n> ")
        price = input("Price?\n> ")
        self.menu_repo.create_menu_item(name, number, description, ingredients, price) # appends inputs to menu_list
        print(f"{name} has been added")
        
    
    def delete_item(self):
        item_num = int(input("Enter the number of the item you wish to remove.\n> "))
        removed_item = item_num - 1
        del self.menu_repo.menu_list[removed_item]
        # self.menu_repo.menu_list.remove(removed_item)
        print(f"\nItem number {item_num} was removed")


    def list_items(self):
        current_list = self.menu_repo.get_menu_list() # returns menu_list and assigns to var
        if current_list == []: # checks for empty list
            print("\nNo items in list!") # prints str if list empty 
        else:
            for food_i in current_list: # goes through every food item in list
                print(food_i)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ") # choice becomes user's input
            action = self.choice.get(choice) # gets value from dictionary choice
            if action:
                action() # value is called
            else:
                print(f"\n{choice} is not a valid option")

if __name__ == "__main__":
    menu = MainMenu() # instance of MainMenu
    menu.run() # calls run
