from prac_06.guitar import Guitar

def run_tests():
    """Create tests for guitar class."""
    guitar = Guitar("Gibson L-5 CES",1922,16035.40)
    another_guitar = Guitar("Gibson Les Paul Tribute Plus" ,2016,1299.00)

    print(f"Gibson L-5 CES get age() - Expected 100. Got {guitar.get_age()}")
    print(f"Another Guiter get_age() - Expected 6. Got {guitar.get_age()}")


run_tests()


