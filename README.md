# Setup Instructions

- create a virtual environment
- Activate the virtual environment
- Install the dependencies located in the `requirements.txt` file.

Throughout the code, you may see places marked with the word `TODO`. Please try to do what you are asked to do.

To run your tests, use the following command:

```
python3 -m unittest
```

If you prefer to use Pytest, you can run:

```
pytest -v
```


You have been provided with a file called `app.py`. Some basic sample code has been included.

## Question 1

Design a constructor for the `Location` class inside the `app.py` file, it takes two values `name` and `number_of_people`.
- Doing this correctly, it wil get one of our tests to pass
- Add a test case to your `LocationTest` to confirm that a location's name is 
correct. The missing test is called `test_location_name`.


## Question 2

Design a method in the `Continent` class called, `add()`. This method will be used to add to the list of countries, `self.countries`.

This method should be able to take in a single argument 

How will you use this class?

```python
location = Location('Berlin', 1000)
continent = Continent('Europe')  
continent.add(location)
```

To see the countries in the continent, you can print

```python
print(continent.countries)    
```

Hint: How do we add items to a list?
