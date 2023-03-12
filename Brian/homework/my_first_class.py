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

class Sloth:

    def __init__(self, name, age, species, color, sound, happy, sad):

        self.name = name
        self.age = age
        self.species = species
        self.color = color
        self.sound = sound
        self.happy = happy
        self.sad = sad

    def get_happy(self):
        if self.age < 2011:
            self.happy = True
        else:
            self.sad = False

        return self.happy

    def set_name(self, sloth):
        self.name = sloth

    def set_age(self, twelve):
        self.age = 13

    def set_species(self, bradypuspygmaeus):
        self.species = bradypuspygmaeus

    def set_color(self, brown):
        self.color = brown

    def set_sound(self, squeak):
        self.sound = squeak

    def set_happy(self, yes):
        self.happy = yes

    def set_sad(self, no):
        self.sad = no

        return True


