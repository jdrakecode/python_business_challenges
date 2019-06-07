# Komodo Insurance Interface
from ki_br import BadgeRepository

class MainMenu:
    def __init__(self):
        self.badge_repo = BadgeRepository()
        self.choice = {
            "1": self.add_badge,
            "2": self.update_badge,
            "3": self.show_all,
            "4": exit
        }

    def display_menu(self):
        print(
"""
Choose a menu item:
1. Add a badge
2. Update a badge
3. Show all badges
4. Exit
"""
        )

    def add_badge(self):
        badge_number = input("Input badge number:\n> ")
        door = input("Input a door that it needs access to:\n> ")
        self.badge_repo.create_badge(badge_number, door)
        for k, v in self.badge_repo.badge_dict.items():
                    print(k, "  --  ", v)

    def update_badge(self):
        print("Select an option")
        while True:
            choice = input("1. Add a door\n2. Remove a door\n> ")
            print("\nBadge # --  Door Access")
            for k, v in self.badge_repo.badge_dict.items():
                print(k, "  --  ", v)
            if choice == "1":
                badge_number = input("\nEnter a badge number to update:\n> ")
                door = input("Input a door that it needs access to:\n> ")
                for k, v in self.badge_repo.badge_dict.items():
                    if str(k) == badge_number:
                        v.append(door)
                for k, v in self.badge_repo.badge_dict.items():
                    print(k, "  --  ", v)
                break
            elif choice == "2":
                badge_number = input("\nEnter a badge number to update:\n> ")
                door = input("Input a door to delete:\n> ")
                for k, v in self.badge_repo.badge_dict.items():
                    if str(k) == badge_number:
                        a = v.index(door)
                        del v[a]
                for k, v in self.badge_repo.badge_dict.items():
                    print(k, "  --  ", v)
                break
            else:
                print("\nPlease enter a valid option (1 or 2)")
            
    def show_all(self):
        print("Badge # --  Door Access")
        for k, v in self.badge_repo.badge_dict.items():
            print(k, "  --  ", v)

    def run(self):
        while True:
            self.display_menu()
            choice = input("> ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print(f"\n{choice} is not a valid option")

if __name__ == "__main__":
    menu = MainMenu()
    menu.run()