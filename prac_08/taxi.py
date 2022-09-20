"""
CP1404/CP5632 Practical
Car class
"""
from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23     #class variable

    def __init__(self, name, fuel, price_per_km):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)     # pass into parent constructer(inherit name, fuel,odometer)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0
        #5 attributes that the taxi has compared to car's attributes

    def __str__(self):      #override parent's __Str__
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

# will also inherit drive(), add_fuel(), __str__(),__init__()
#__str__() and init are overidden -> provide more specialized implementations of your own

    def get_fare(self):     #taxi only
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven