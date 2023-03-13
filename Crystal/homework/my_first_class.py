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
    def __init__(self, name, age, species, color, sound, animal_happy, animal_sad):
        self.name = name
        self.age = age
        self.species = species
        self.color = color
        self.sound = sound
        self.animal_happy = animal_happy
        self.animal_sad = animal_sad

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_species(self):
        return self.species

    def get_color(self):
        return self.color

    def get_sound(self):
        return self.sound

    def get_animal_happy(self):
        return self.animal_happy

    def get_animal_sad(self):
        return self.animal_sad


crystals_son = Animal(
    name="Olaf",
    age=8,
    species="dog",
    color="white",
    sound="awoo",
    animal_happy="Olaf is happy boi",
    animal_sad="Olaf is sad boi"
)

# print(crystals_son.get_name())
# print(crystals_son.get_animal_happy())
# print(crystals_son.get_animal_sad())
# print(crystals_son.get_sound())

# print("What sound does", crystals_son.name, "make when they are happy?")
# print(crystals_son.get_sound())

print(crystals_son.get_animal_sad())
