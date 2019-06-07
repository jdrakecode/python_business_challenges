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
        pass

    def update_badge(self):
        pass

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