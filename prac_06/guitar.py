from datetime import datetime

year = 2022
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        return f"{self.name}({self.year}) : ${self.cost}"

    def get_age(self):
        today = datetime.today()
        age = today.year - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE







