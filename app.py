class Location:
    def __init__(self, name, number_of_people) -> None:
        self.name = name
        self.number_of_people = number_of_people

    def __repr__(self):
        return f"<Name: {self.name}, population: {self.number_of_people}>"


class Continent:
    def __init__(self, name) -> None:
        self.name = name
        self.countries = []  # Countries is a list of location instances.

    def add(self, countries):
        self.countries.append(countries)
        return self.countries

    def __repr__(self) -> str:
        return self.name


location = Location("Berlin", 1000)
continent = Continent("Europe")
continent.add(location)
print(continent.countries)
