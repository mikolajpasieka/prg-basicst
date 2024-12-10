class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"The distance is {self.distance()}")
        print(f"The fare is {self.fare()}")

def main():
    # your program
    ride1 = TaxiRide()
    ride2 = TaxiRide()
    ride1.rate_per_km = 5
    ride2.rate_per_km = 4
    ride1.distance = 50
    ride2.distance = 27
    ride1.fare = calculate_fare(5, 50)
    ride2.fare = calculate_fare(4, 27)
    print(print_receipt(ride1))
    print(print_receipt(ride2))





if __name__ == "__main__":
    main()
