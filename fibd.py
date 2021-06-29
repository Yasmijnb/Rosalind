#! /usr/env python3
"""
Author: Yasmijn Balder

Rosalind problem: fibd
This function returns the last occurrence of a fibonacci sequence which is
made using a range and a number of offspring
"""

from sys import argv


def fibonacci(n, m):
    """Returns an int with the number of rabbits after n months.

    Keyword arguments:
    n -- int, a number to define the range of the sequence
    m -- int, a number to define the amount of months each rabbit lives
    """

    # Start with 1 rabbit that is 1 month old
    rabbits = [1]

    # Make sure that the input is read as integers
    n = int(n)
    m = int(m)

    # Loop throught the given time range
    for number in range(n):
        # Make an empty list for new babies
        babies = []
        # Enumerate through the currently alive rabbits
        for ind, rabbit in enumerate(rabbits):
            # If the rabbit is one years old, it will not have offspring
            if rabbit == 1:
                # Make the rabbit older
                rabbits[ind] = rabbit + 1
            # If the rabbit is between 1 and m, it will have offspring and live
            elif rabbit > 1 and rabbit < m:
                # Make the rabbit older
                rabbits[ind] = rabbit + 1
                # Add a new baby
                babies.append(1)
            # If the rabbit is old, it will have offspring and die
            elif rabbit == m:
                # Remove the rabbit
                rabbits.pop(ind)
                # Add a new baby
                babies.append(1)
        # Add the new rabbits
        rabbits = rabbits + babies

    # Returns the number of rabbits that are alive after n months
    return len(rabbits)


def main():
    """This code will be executed when called from the command line
    """
    # Step 1: Assign input to variables
    with open(argv[1]) as f:
        for line in f:
            items = line.split()
            n = items[0]
            m = items[1]

    # Step 2: Obtain the number of alive rabbits
    fib_list = fibonacci(n, m)

    # Step 3: Print the output
    print('Number of rabbits =', fib_list)


if __name__ == "__main__":
    main()
