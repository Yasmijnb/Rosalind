#! /usr/env python3
"""
Author: Yasmijn Balder
Rosalind problem: ini
This function returns the number of A C G and T nucleotides given in a string,
in alphabetical order, separated by a space.
"""

from sys import argv


def occurences_in_string(sequence):
    """Returns a dictionary with the unique characters as key and the number of
    occurences as value. The dictionary keys are alphabetically sorted.

    Keyword arguments:
    sequence -- a string
    """

    # Create an empty dictionary to store the unique characters and occurences
    occ_dict = {}

    # Find the unique characters
    unique = list(set(sequence))

    # Sort alphabetically
    sorted_unique = sorted(unique)

    # Find the number of occurences for each unique character
    for character in sorted_unique:
        occ_dict[character] = sequence.count(character)

    return occ_dict

def main():
    """This code will be executed when called from the command line
    """
    # Step 1: Assign input to variables
    with open(argv[1]) as input_file:
        for line in input_file:
            seq = line.strip()

    # Step 2: Obtain the number of occurences per character
    occurences = occurences_in_string(seq)

    # Step 3: Print the total number of components
    print(" ".join(map(str, occurences.values())))

if __name__ == "__main__":
    main()
