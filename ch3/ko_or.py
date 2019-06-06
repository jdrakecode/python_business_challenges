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
        self.combined_list = []

    # def combine(self, event_type, event_cost):
    #     combined_costs = Outings(event_type, event_cost)
    #     self.combined_list.append(combined_costs)