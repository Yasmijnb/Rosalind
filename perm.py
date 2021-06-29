#! /usr/env python3
"""
Author: Yasmijn Balder

Rosalind problem: perm
Finds the permutations of a given length.
Prints the number of unique permutations of the given length, followed by all
the permutations on a new line, separated by spaces.
"""

import math
from itertools import permutations
from sys import argv


def permutation_list(length):
    """Returns a list with tuples. The tuples contain integers in all possible
    orders, of the given length

    Keyword arguments
    length -- int, a positive number for the length of permutations
    """

    # Initiate an empty list to store all positive numbers up to the length
    all = []
    # Go through all positive numbers up to the length
    for number in range(1, length + 1):
        # Add each number to the list
        all.append(number)

    # Find all permutations with the use of intertools
    perms = list(permutations(all))

    return perms


def main():
    """This code will be executed when called from the command line
    """

    # Step 1: Assign input to variables
    with open(argv[1]) as f:
        for line in f:
            items = line.split()
    # Make sure the input is seen as an integer
    pi = int(items[0])

    # Step 2: Obtain the permutation list
    enumerations = permutation_list(pi)

    # Step 3: Print the output
    print(math.factorial(pi))
    for combination in enumerations:
        print(" ".join(map(str, combination)))


if __name__ == "__main__":
    main()
