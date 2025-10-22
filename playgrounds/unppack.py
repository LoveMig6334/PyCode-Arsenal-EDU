"""
Python Unpacking Tutorial
-------------------------
This module demonstrates various unpacking techniques in Python.
Unpacking allows you to extract individual elements from collections like lists.
"""

import random

# Create a sample list of numbers from 1 to 10
number_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Printing the list as a whole - will show with brackets
print("Printing the entire list:")
print(number_lst)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using the * operator to unpack the list into individual arguments
# This removes the brackets and commas from the output
print("Unpacking the list with the * operator:")
print(*number_lst)  # Output: 1 2 3 4 5 6 7 8 9 10

# Creating a new list using list comprehension - this is an alternative
# way to process each element of a list individually
unpack = [number * 2 for number in number_lst]
print(f"Unpack list using list comprehension: {unpack}")


def unpack_test() -> None:
    """
    Demonstrates different ways to iterate through and unpack lists.

    This function shows:
    1. Using the * operator to unpack a list into print()
    2. Iterating through a list with a for loop
    """
    print("\nTest function for unpacking")

    # Method 1: Unpacking with * operator
    print("Unpacking with *:")
    print(*number_lst)  # Output: 1 2 3 4 5 6 7 8 9 10

    # Method 2: Iterating through list elements
    print("Iterating through elements:")
    for number in number_lst:
        print(number, end=" ")  # Print each number with a space

    # Print a newline to end the output cleanly
    print()


def return_function() -> list[int]:
    """
    Generates and returns a list of 5 random integers between 1 and 9.

    Returns:
        list[int]: A list containing 5 random integers
    """
    # random.sample selects unique elements from the specified range
    random_list_number = random.sample(range(1, 10), 5)

    return random_list_number


# Call the function and store the returned random numbers
random_numbers = return_function()
print("\nRandomly generated numbers (unpacked):")
print(*random_numbers)  # Unpack and print the random numbers

# Call the unpack_test function to demonstrate unpacking methods
unpack_test()


def test_function(*args):
    """
    Demonstrates the use of *args parameter which collects multiple
    arguments into a tuple.

    Args:
        *args: Variable number of arguments
    """
    print("\nDemonstrating *args parameter:")
    for arg in args:
        print(arg, end=" ")
    print()  # Add a newline at the end


# Demonstrate calling a function with multiple arguments
# which are collected using *args in the function
print("\nCalling test_function with multiple arguments:")
test_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
