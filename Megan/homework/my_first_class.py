"""
For this assignment, I want you to write a class that creates an animal Object.
Use your imagination on what you want to include, but make sure to include
the following attributes:

- name
- age
- species
- color
- sound (what sound do they make)

And make sure to include the following methods:
- get_name
- get_age
- get_species
- get_color
- get_sound
- get_animal_happy (this should return a string that says "animal_name is happy")
- get_animal_sad (this should return a string that says "animal_name is sad")

An example of this is available in lessons/learning_classes.py
"""


# Place your code here

class Animal:
    """Class definition that defines an Animal object and it's attributes"""

def __init__(self, name, age, species, color, sound, happy, sad):
    """The constructor method for the Animal class"""
    self.name = name
    self.age = age
    self.species = species
    self.color = color
    self.sound = sound
    self.happy = happy
    self.sad = sad

def get_name(self):
    """Simple 'get' method to return the Animal's name"""
    return self.name

def get_age(self):
    """Simple 'get' method to return the Animal's age"""
    return self.age

def get_species(self):
    """Simple 'get' method to return the Animal's species"""
    return self.species

def get_color(self):
    """Simple 'get' method to return the Animal's color"""
    return self.color

def get_sound(self):
    """Simple 'get' method to return the Animal's sound"""
    return self.sound

def get_animal_happy(self):
    response = f"{self.name} is happy"

def get_animal_sad(self):
    response = f"{self.name} is sad"

best_animal_ever = Animal(
    name="Dolly",
    age=5,
    species="dolphin",
    color="pink",
    sound="EEeeeEEEeee",
    mood="happy" and "sad"
)

best_animal_ever.get_name

best_animal_ever.get_age

best_animal_ever.get_species

best_animal_ever.get_color

best_animal_ever.get_sound

best_animal_ever.get_animal_happy

best_animal_ever.get_animal_sad

git commit - am 'megan-learning-classes'
git push
