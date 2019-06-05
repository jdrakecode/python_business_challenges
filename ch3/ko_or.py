# Komodo Outings - Outings Repository

class Outings:
    def __init__(self, event_date, event_type, event_cost, num_people, cost_person):
        self.event_date = event_date
        self.event_type = event_type
        self.event_cost = event_cost
        self.num_people = num_people
        self.cost_person = cost_person

    def __repr__(self):
        return f"{self.event_date} {self.event_type} {self.event_cost} {self.num_people} {self.cost_person}"

class OutingsRepository:
    def __init__(self):
        self.outings_list = []
        # self.e_d = ""
        # self.e_t = ""
        # self.e_c = ""
        # self.n_p = ""
        # self.c_p = ""
    
    # def create_outing (self, event_date, event_type, event_cost, num_people, cost_person):
    #     new_outing = Outings(event_date, event_type, event_cost, num_people, cost_person)
    #     self.outings_list.append(new_outing)
