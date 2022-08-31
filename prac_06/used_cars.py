"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Tesla X", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car("Rolls Royce", 100)

    # Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)

    # Print the amount of fuel in the car.
    print(f"Fuel in limo: {limo.fuel}")

    # Attempt to drive the car 115 km using the drive method.
    limo.drive(115)

    # Print the car's odometer reading.
    print(f"Odemeter in limo after driving:{limo.odometer}")
    print(f"Fuel in limo after driving:{limo.fuel}")

    # Now add the __str__ method to the Car class in car.py.Using {} string formatting,
    # have it return a string in the following format:Car, fuel=42, odometer=277
    # Remember that you can run this method by printing your car object, or passing the car object to the str() function.
    # Do NOT call the method explicitly like my_car.__str__()

    # Now add a name field to the Car class (in car.py), and adjust the __init__ and __str__ methods to set and display this respectively.
    # Make the str method return the car's name instead of just "Car".
    # Now add names (literals) to the constructors where you create Car objects in the used_cars.py program.
    # Test your work and make sure you can now make and view named cars.

    # In your used_cars.py program, just print your car object/s to make sure that the __str__ method is working as expected.
    print(limo)


main()
