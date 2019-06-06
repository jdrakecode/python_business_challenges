# Komodo Outings - Outings Repository

class OutingsCost:
    def __init__(self, event_cost):
        self.event_cost = event_cost

    def __repr__(self):
        return f"{self.event_cost}"

class OutingsRepository:
    def __init__(self):
        self.cost_list = []
        self.golf_list = []
        self.bowling_list = []
        self.park_list = []
        self.concert_list = []
        self.cost_type_list = []

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
            
    def cost_by_type(self, event_type, event_cost):
        if event_type == "golf":
            for i in self.golf_list:
                event_cost += i
                self.golf_list.pop()
            self.golf_list.append(event_cost)
        elif event_type == "bowling":
            for i in self.bowling_list:
                event_cost += i
                self.bowling_list.pop()
            self.bowling_list.append(event_cost)
        elif event_type == "amusement park":
            for i in self.park_list:
                event_cost += i
                self.park_list.pop()
            self.park_list.append(event_cost)
        elif event_type == "concert":
            for i in self.concert_list:
                event_cost += i
                self.concert_list.pop()
            self.concert_list.append(event_cost)
