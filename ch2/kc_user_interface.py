# Interface for Komodo Claims
from komodo_claims import ClaimRepository

class MainMenu:
    def __init__(self):
        self.claim_repo = ClaimRepository()
        self.choice = {
            "1": self.see_all,
            "2": self.next_claim,
            "3": self.new_claim,
            "4": exit
        }

    def display_menu(self):
        print(
"""
Choose a menu item:
1. See all claims
2. Take care of next claim
3. Enter a new claim
4. Exit
"""
        )
    
    def see_all(self):
        cl = self.claim_repo.claim_list
        if cl != []:
            print("\nClaimID  |  Type  |  Amount  |  DateOfAccident  |  DateOfClaim  |  IsValid  |  Description")
            cl = self.claim_repo.claim_list
            for i in cl:
                print(i)
        else:
            print("\nFortunately, claims list is empty!")

    def next_claim(self):
        while True:
            cl = self.claim_repo.claim_list
            if cl != []:
                print("\nClaimID  |  Type  |  Amount  |  DateOfAccident  |  DateOfClaim  |  IsValid  |  Description\n", cl[0])
                yorn = input("\nDo you want to deal with this claim now (y/n)?\n> ")
                if yorn == "y":
                    print("\nClaim taken.")
                    del cl[0]
                    if cl != []:
                        print("\nNext claim:")
                        continue
                    else:
                        continue
                elif yorn == "n":
                    menu.run()
                else:
                    print("\nPlease enter y for Yes or n for No")
                    continue
            else:
                print("\nClaims list is empty!")
                break

    def new_claim(self):
        claim_id = input("Enter claim id:\n> ") # Stretch Goal: assign by increments of 1 instead of input
        claim_type = input("Enter claim type:\n> ")
        amount = input("Amount of Damage:\n> ")
        date_accident = input("Date of Accident:\n> ")
        date_claim = input("Date of Claim:\n> ")
        is_valid = input("Claim made within 30 days?\nEnter True or False:\n> ") # Stretch Goal: change to check for t/n and y/n also
        description = input("Enter a claim description:\n> ")
        self.claim_repo.create_claim(claim_id, claim_type, amount, date_accident, date_claim, is_valid, description)
        print(f"Claim number {claim_id} has been added")

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
