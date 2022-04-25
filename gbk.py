#! /usr/env python3
"""
Author: Yasmijn Balder
Rosalind problem: gbk
Returns the number of Nucleotide Genbank entries for a given genus within two
dates.
"""

from sys import argv
from Bio import Entrez

def CountGenbankEntries(genus, database, species='', start='', end=''):
    """Returns the number of entries in the genbank database given the genus
    and optional other specifications

    Keyword arguments:
    genus -- string, specifying the genus
    database -- database to search in
    species -- string, optional, specifying the species
    start -- string, optional, to find entries published after this date
    end -- string, optional, to find entries published before this date
    """

    Entrez.email = "yasmijn.balder@hotmail.com"
    handle = Entrez.esearch(db = database, \
        term = ' '.join([genus, species, "[Organism]"]), \
            datetype = 'pdat', mindate = start, maxdate = end)
    record = Entrez.read(handle)
    entries = record["Count"]

    return entries

def main():
    """This code will be executed when called from the command line
    """
    # Step 1: Assign input to variables
    genus = ''
    start_date = ''
    end_date = ''
    with open(argv[1]) as input_file:
        for line in input_file:
            if genus == '':
                genus = line.strip()
            elif start_date == '':
                start_date = line.strip()
            else:
                end_date = line.strip()

    # Step 2: Obtain the number of occurences in the GenBank database
    occurences = CountGenbankEntries(genus, 'nucleotide', start=start_date, end=end_date)


    # Step 3: Print the total number of entries
    print(occurences)

if __name__ == "__main__":
    main()
