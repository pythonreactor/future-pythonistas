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
"""


╭╮╱╱╭━━━┳━━━┳━━━━╮╭━━━┳╮╱╱╭━━┳━━━━┳━━━━┳╮╱╱╭╮
┃┃╱╱┃╭━╮┃╭━╮┃╭╮╭╮┃┃╭━╮┃┃╱╱╰┫┣┻━━╮━┣━━╮━┃╰╮╭╯┃
┃┃╱╱┃┃╱┃┃╰━━╋╯┃┃╰╯┃┃╱╰┫┃╱╱╱┃┃╱╱╭╯╭╯╱╭╯╭┻╮╰╯╭╯
┃┃╱╭┫┃╱┃┣━━╮┃╱┃┃╱╱┃┃╭━┫┃╱╭╮┃┃╱╭╯╭╯╱╭╯╭╯╱╰╮╭╯
┃╰━╯┃╰━╯┃╰━╯┃╱┃┃╱╱┃╰┻━┃╰━╯┣┫┣┳╯━╰━┳╯━╰━╮╱┃┃
╰━━━┻━━━┻━━━╯╱╰╯╱╱╰━━━┻━━━┻━━┻━━━━┻━━━━╯╱╰╯


"""

class Animal:

    def __init__(self, name, age, species, color, sound, happy, sad):

        self.name = name
        self.age = age
        self.species = species
        self.color = color
        self.sound = sound
        self.happy = happy
        self.sad = sad


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
        response = f"{self.name} is happy"
        return response

    def get_animal_sad(self):
        response = f"{self.name} is not sad"
        return response

animal_ruler = Animal(
    name="sloth",
    age=13,
    species="bradypus pygmaeus",
    color="grey",
    sound="squeak",
    happy="yes",
    sad="no"
)

print(animal_ruler.get_name())
print(animal_ruler.get_age())
print(animal_ruler.get_species())
print(animal_ruler.get_color())
print(animal_ruler.get_sound())
print(animal_ruler.get_animal_happy())
print(animal_ruler.get_animal_sad())
