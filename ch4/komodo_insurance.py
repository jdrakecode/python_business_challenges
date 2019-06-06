# Komodo Insurance Interface

class MainMenu:
    def __init__(self):
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
        pass