# Komodo Outings Interface
from ko_or import OutingsRepository
from prettytable import PrettyTable

class MainMenu:
    def __init__(self):
        self.out_rep = OutingsRepository()
        self.pretty_table = PrettyTable()
        self.choice = {
            "1": self.display_all,
            "2": self.add_outing,
            "3": self.display_cost,
            "4": exit,
        }

    def display_menu(self):
        print(
"""
Choose a menu item:
1. Display list of outings
2. Add outing to list
3. Display combined cost
4. Exit
"""
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input("> ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print(f"\n{choice} is not a valid option")

    def display_all(self):
        if self.pretty_table.field_names == []:
            print("\nEvent list is empty! Please add an event.")
        else:
            print(self.pretty_table)

    def add_outing(self):
        event_date = input("Enter event date:\n> ")
        event_type = input("Enter event type:\n> ")
        num_people = int(input("Number of people:\n> ")) # breaks if input is not a number
        cost_person = float(input("Cost per person:\n> ")) # breaks if input is not a number
        event_cost = cost_person * num_people
        self.pretty_table.field_names = ["Event Date", "Event Type", "Event Cost", "Number of People", "Cost per Person"]  # could move this outside
        self.pretty_table.add_row([event_date, event_type, event_cost, num_people, cost_person])
        self.out_rep.combine_costs(event_cost)
        print(f"\n{event_type} event has been added")
        print(self.pretty_table) # spacing offset by one space if <print(f"\n{event_type} event has been added\n", self.pretty_table)> is used - reason unkown

    def display_cost(self): 
        self.out_rep.convert_list()
            

if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
