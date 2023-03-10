# Classes

One of the hardest parts about a class is understanding 3 things:

1. Attributes
2. Methods
3. Self

Please refer to this Class definition when reading the next 3 explanations:

```python
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
```

## Attributes
An attribute is a value that belongs to the given instance of a class OBJECT.
Defining a class and creating an object are mutually inclusive.You must define a Class before
creating an Object.

An attribute would be something like make & model of a car Object.
In the above example, `self.make` would be an attribute of the Car class .

## Methods

A method is a function within a class . It is something you can use to return values of an attribute
or set the value of one or many attributes for the GIVEN OBJECT.

Given Object means the object you have created as an instance of the class. An example of creating an
object using the above class is:

```python
my_first_car = Car(
    make="Ford",
    model="Mustang",
    year=1971,
    color="Silver",
    mpg=6.3
)
```

Now, `my_first_car` is an instance of the Car class. Create a second one to see the differences:

```python
my_second_car = Car(
    make="Porsche",
    model="911 S",
    year=1973,
    color="Silver",
    mpg=9
)
```

Now, there are 2 ways to see the values for the given attributes in the provided class:

### Getting an Object Attribute Value

#### Way 1 - Dot Operation
`my_first_car.year` and this would return 1971.

#### Way 2 - Get Method

`my_first_car.get_year` - this would return 1971, but also set `my_first_car.old` to `True`.

Inherently, you don't need a get method to get the values of given attributes for an object.
However, it is good practice because there are times when getting an attribute value involves more
than just pulling the actual value. Sometimes there are other checks that need to be made in order
to return a proper value and sometimes other values in the system need to be updated each time you
get the attribute. So, **GET IN THE HABIT**.

If you did the same as above for `my_second_car`, you would see different values returned. That is
because each time you create an instance of a `Class`, you are creating a NEW `Object`.

## Self

This is probably the most important thing to understand.And I will do my best to explain.
`self` is a reference to the object that was created. This is why `my_first_car` and `my_second_car`
have different values inside of them when you ask for something about itSELF.

You cannot do something like, `self.year` outside of the `Class`, because `self` doesn't refer to
anything unless inside an `Object`.

Let's look at the `__init__` constructor first in the given example above.

### Class Construction

`self.year = year` -> This is saying that this object's year attribute will be equal to the value passed
in when creating this object.

It is also important to note what parameters are used when creating the `__init__` constructor method:

    def __init__(self, make, model, year, color, mpg)


You must note which values you are going to take in when creating a new object. Here, I chose to use `make`,
`model`, `year`, `color`, `mpg`. They must be descriptive so others don't get confused. And below that, I am setting
this instance's values when creating a new object.


# BONUS

## DOT OPERATION

This is a way of accessing values or methods within an object: `my_first_car.mpg` < - see the `.` before mpg?
That means, for the `my_first_car` object, enter into it and return to me the `mpg` value.

Dot Operation is also used for using methods. A quick example is something some of you may have seen during the last
homework when using the `statistics` library.

`statistics.mean`, although I think those that used this just imported `mean` from the `statistics` library. They both
work the same.

```python
from statistics import mean

result = mean([1, 2, 3, 4, 5])
```

Is the same as:

```python
import statistics

# Note the DOT NOTATION to access the mean method
result = statistics.mean([1, 2, 3, 4, 5])
```