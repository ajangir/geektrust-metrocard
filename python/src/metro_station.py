class MetroStation:
    def __init__(self, name):
        self.name = name
        self.passenger_summary = {}
        self.total_collection = 0
        self.total_discount_given = 0
    
    def add_collection(self,collection,discount=0):
        self.total_collection += collection
        self.total_discount_given += discount
    
    def collect_travel_charge(self, passenger_type, journey_type):
        if passenger_type not in self.passenger_summary:
            self.passenger_summary[passenger_type] = 0

        travel_charge = self.get_travel_charge(passenger_type, journey_type)

        self.passenger_summary[passenger_type] += 1
        self.total_collection += travel_charge

        if journey_type == 'RETURN':
            self.total_discount_given += travel_charge / 2

    def get_travel_charge(self, passenger_type, journey_type):
        if passenger_type == 'ADULT':
            return 200 if journey_type == 'SINGLE' else 100
        elif passenger_type == 'SENIOR_CITIZEN':
            return 100 if journey_type == 'SINGLE' else 50
        elif passenger_type == 'KID':
            return 50 if journey_type == 'SINGLE' else 25
        return 0

    def print_summary(self):
        print(f"TOTAL_COLLECTION {self.name} {self.total_collection} {self.total_discount_given}")
        sorted_summary = sorted(self.passenger_summary.items(), key=lambda x: (-x[1], x[0]))
        for passenger_type, count in sorted_summary:
            print(f"{passenger_type} {count}")
