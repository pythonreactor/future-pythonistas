"""
For this assignment, I want you to write a function that takes in a list of
numbers and returns the sum of the numbers in the list.

An example of this in pseudocode would be:

def some_function(list_of_numbers):
    # do something with the list of numbers

    return sum_of_numbers


I would also like for you to create another function under that one that uses
the first function to return the average of the numbers in the list.

An example of this in pseudocode would be:

def some_other_function(list_of_numbers):
    # Get the sum of all numbers in the list
    # Get the average of the numbers in the list (sum / number of numbers)

    return average_of_numbers

"""

# Place your code here:
def sum_numbers(list_of_numbers):
    return sum(list_of_numbers)

list_of_numbers = [1, 2, 3, 4]
result = sum_numbers(list_of_numbers)
print("the sum of the numbers is =", result)


def average(list_of_numbers):
    total = sum(list_of_numbers)
    return total/len(list_of_numbers)


result = average(list_of_numbers)
print("the average of the numbers is =", result)


