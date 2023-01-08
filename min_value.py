#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: December 16 2022
# This program generates random numbers, adds
# them to a list, and then finds
# and displays the minimum value


import random
import constants


# This function returns the minimum value in the array
def find_min_value(ran_list_integers):
    # Initialize the variable to -1
    min_value = -1

    # Iterate through list to find min value
    for index in ran_list_integers:
        # Check if the index is less than the current min value
        if index < min_value:
            # If true, assign it as the new min value
            min_value = index

    # Returns the min value
    return min_value


# Function to populate a list with randomly generated numbers
def main():
    # Initialize empty list
    list_of_ints = []

    # Loop to generate ten random numbers
    for counter in range(constants.MAX_LIST_SIZE):
        # Generate a random number from 0-100 and append it to the list
        list_of_ints.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))
        # Display the number added and its position
        print(f"{list_of_ints[counter]} added to the list at position {counter}")

    # Calls function return the min value
    min_value = find_min_value(list_of_ints)
    # Display the min value
    print(f"The min value: {min_value}")


if __name__ == "__main__":
    main()
