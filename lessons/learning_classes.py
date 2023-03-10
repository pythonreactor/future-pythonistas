class Car:
    """Class definition that defines a Car object and its attributes"""

    def __init__(self, make, model, year, color, mpg):
        """The constructor method for the Car class"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mpg = mpg

        self.old = False

    def get_year(self):
        """Simple `get` method to return the Car object's year"""
        if self.year < 2020:
            self.old = True
        else:
            self.old = False

        return self.year

    def set_year(self, year):
        """Simple `set` method to set the Car object's year after creation"""
        self.year = year

        # This return statement isn't necessary, but it is a good visual aid
        return True

# If you'd like to see this class in action, feel free to add some class
# creation code below and run this file directly using:
# `python3 some/path/to/this/learning_classes.py`
