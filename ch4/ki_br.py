# Komodo Insurance Badge Repository

class Badge:
    def __init__(self, badge_number):
        self.badge_number = badge_number

    def __repr__(self):
        return f"{self.badge_number}"

class Door:
    def __init__(self, door):
        self.door = door

    def __repr__(self):
        return f"{self.door}"

class BadgeRepository:
    def __init__(self):
        self.badge_dict = {"90561" : ["a1", "a2", "a3", "a4", "a5"], "67690" : ["b6", "b7", "b8", "b9"]}
    
    def create_badge(self, badge_number, door):
        new_door = []
        new_badge = Badge(badge_number)
        dd = Door(door)
        d = str(dd)
        new_door.append(d)
        yorn = input("Add another door? (y/n)\n> ")
        while yorn == "y":
            door = input("Input a door that it needs access to:\n> ")
            new_door.append(door)
            yorn = input("Add another door? (y/n)\n> ")
            if yorn == "n":
                break
            continue
        self.badge_dict.update({new_badge:new_door})
            