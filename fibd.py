#! /usr/env python3
"""
Author: Yasmijn Balder

This is function returns the last occurrence of a fibonacci sequence \
which is made using a range and a number of offspring
"""

from sys import argv

def fibonacci(n, m):
    """
    Returns a fibonacci sequence for range of n with k number of offspring!!!!!!!!!!!!!!

    Keyword arguments:
    n: a number to define the range of the sequence
    m: a number to define the amount of months each rabbit lives
    """
    
    # Start with 1 rabbit that is 1 month old
    rabbits = [1]
    
    # Make sure that the input is read as integers
    n = int(n)
    m = int(m)


    for number in range(n):
        for rabbit in rabbits:
            if rabbit == 1:
                # Make the rabbit older
                print(rabbit)
            elif rabbit > 1 and rabbit < m:
                # Make the rabbit older
                # Add a new baby
                rabbits.append(1)
            elif rabbit == m:
                # Remove the rabbit
                # Add a new baby
                rabbits.append(1)

    print(len(rabbits))
    return len(rabbits)

def main():
    """This code will be executed when called from the command line
    """
#step 1: assign input to variables
    with open(argv[1]) as f:
        for line in f:
            items = line.split()
            n = items[0]
            print(n)
            m = items[1]
            print(m)
            
#step 2: make a fibonacci sequence using the variables
    fib_list = fibonacci(n, m)
    
#step 3: print the last occurrence in the fibonacci sequence
    print('Number of rabbits =', fib_list)

if __name__ == "__main__":
    main()
