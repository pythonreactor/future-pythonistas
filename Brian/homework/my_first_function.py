"""
For this assignment, I want you to write a function that takes in a list of
numbers and returns the sum of the numbers in the list.

An example of this in pseudocode would be:

def some_function(list_of_numbers):
    # do something with the list of numbers
    return sum_of_numbers
"""

"""
╭━━━┳╮╱╱╭━━┳━━━━┳━━━━┳╮╱╱╭╮╭━━━┳━━━┳━━━┳━━━┳━━┳━━━╮
┃╭━╮┃┃╱╱╰┫┣┻━━╮━┣━━╮━┃╰╮╭╯┃┃╭━╮┃╭━╮┃╭━╮┃╭━╮┣┫┣┫╭━╮┃
┃┃╱╰┫┃╱╱╱┃┃╱╱╭╯╭╯╱╭╯╭┻╮╰╯╭╯┃┃╱╰┫┃╱┃┃╰━━┫╰━━╮┃┃┃╰━╯┃
┃┃╭━┫┃╱╭╮┃┃╱╭╯╭╯╱╭╯╭╯╱╰╮╭╯╱┃┃╭━┫┃╱┃┣━━╮┣━━╮┃┃┃┃╭━━╯
┃╰┻━┃╰━╯┣┫┣┳╯━╰━┳╯━╰━╮╱┃┃╱╱┃╰┻━┃╰━╯┃╰━╯┃╰━╯┣┫┣┫┃
╰━━━┻━━━┻━━┻━━━━┻━━━━╯╱╰╯╱╱╰━━━┻━━━┻━━━┻━━━┻━━┻╯
"""

def sum_numbers(list_of_numbers):
    return sum(list_of_numbers)


list_of_numbers = [1, 2, 3, 4, 5]
result = sum_numbers(list_of_numbers)
print("The sum of the numbers is =", result)

from statistics import mean


def Average(list_of_numbers):
    return mean(lst)


lst = [1, 2, 3, 4, 5]
average = Average(lst)

print("The average of the list =", round(average))
