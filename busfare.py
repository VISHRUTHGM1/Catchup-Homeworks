class Vehicle:
    def __init__(self, seat_count):
        self.seat_count = seat_count

    def default_fare(self):
        fare = self.seat_count * 100  # base fare
        tax = fare * 0.10  # 10% tax
        total_fare = fare + tax
        return total_fare

    def display(self):
        print(f"Total fare: {self.default_fare()}")

class Bus(Vehicle):
    def __init__(self): 
        super().__init__(50)  # A bus has 50 seats

my_bus = Bus()
my_bus.display()
