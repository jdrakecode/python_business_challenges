# Komodo Outings - Outings Repository

class OutingsCost:
    def __init__(self, event_cost):
        self.event_cost = event_cost

    def __repr__(self):
        return f"{self.event_cost}"

class OutingsRepository:
    def __init__(self):
        self.cost_list = []

    def combine_costs(self, event_cost):
        outing_cost = OutingsCost(event_cost)
        self.cost_list.append(outing_cost)

    def convert_list(self):
        a = 0
        for i in self.cost_list:
            x = str(i)
            y = float(x)
            a = a + y
        print(f"\nTotal cost of all outings is ${a}")
            