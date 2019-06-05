# Komodo Claims
#  -> git fetch -> remove tomorrow morning
class Claim:
    def __init__(self, claim_id, claim_type, amount, date_accident, date_claim, is_valid, description):
        self.claim_id = claim_id
        self.claim_type = claim_type
        self.amount = amount
        self.date_accident = date_accident
        self.date_claim = date_claim
        self.is_valid = is_valid
        self.description = description
    
    def __repr__(self):
        return f"{self.claim_id}           {self.claim_type}      {self.amount}         {self.date_accident}            {self.date_claim}         {self.is_valid}        {self.description}"
        # Formats strangely when user inputs are too long or too short
        # ClaimID   Type    Amount  DateOfAccident  DateOfClaim IsValid Description
        # 1         Car     $400    4-25-19         4-27-19     True    Fender Bender     

class ClaimRepository:
    def __init__(self):
        self.claim_list = []
        
    def create_claim(self, claim_id, claim_type, amount, date_accident, date_claim, is_valid, description):
        new_claim = Claim(claim_id, claim_type, amount, date_accident, date_claim, is_valid, description)
        self.claim_list.append(new_claim)
    
    def process_claim(self):
        pass