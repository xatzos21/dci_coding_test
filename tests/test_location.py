import unittest
from app import Location, Continent


class LocationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_location = Location("Berlin", 10000)

    def test_location_number_of_people(self):
        self.assertEqual(self.sample_location.number_of_people, 10000)

    def test_location_name(self):
        self.assertEqual(self.sample_location.name, "Berlin")


# You do not need to change this test
class ContinentTest(unittest.TestCase):
    def test_continent_adding(self):
        location = Location("London", 250000)
        continent = Continent("Europe")
        continent.add(location)
        continent.add(Location("Munich", 500000))
        continent.add(Location("Stockholm", 550000))
        continent.add(Location("Frankfurt", 650000))

        self.assertEqual(len(continent.countries), 4)
        self.assertIsInstance(continent.countries[0], Location)


if __name__ == "__main__":
    unittest.main()
