# Komodo Outings Interface
from ko_or import OutingsRepository#, Outings
from prettytable import PrettyTable

class MainMenu:
    def __init__(self):
        self.outings_repo = OutingsRepository()
        # self.outings = Outings()
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
        pt = self.pretty_table # Creates table every time *CHANGE THIS*
        pt.field_names = ["Event Date", "Event Type", "Event Cost", "Number of People", "Cost per Person"]
        pt.add_row([self.outings_repo.e_d, self.outings_repo.e_t, self.outings_repo.e_c, self.outings_repo.n_p, self.outings_repo.c_p])
        print(pt)
    
    def add_outing(self):
        event_date = input("Enter event date:\n> ")
        event_type = input("Enter event type:\n> ")
        num_people = float(input("Number of people:\n> "))
        cost_person = float(input("Cost per person:\n> "))
        event_cost = cost_person * num_people
        # self.outings_repo.create_outing(event_date, event_type, event_cost, num_people, cost_person)
        self.outings_repo.e_d = f"{event_date}"
        self.outings_repo.e_t = f"{event_type}"
        self.outings_repo.e_c = f"{event_cost}"
        self.outings_repo.n_p = f"{num_people}"
        self.outings_repo.c_p = f"{cost_person}"
        print(f"{event_type} event has been added")

    def display_cost(self):
        pass

if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
