#! /usr/env python3
"""
Author: Yasmijn Balder

Rosalind problem: long
This function returns the shortest superstring containing all given strings
(thus corresponding to a reconstructed chromosome).
"""

from sys import argv
import re

def fasta_parser(fasta_file):
    """Returns a list of lists. Each list represents a sequence, with the name
    as the first item, and the sequence as the second.

    Keyword arguments:
    fasta_file -- a str in fasta format
    """

    # Split the fasta file on lines
    lines = fasta_file.split('\n')
    # Make an empty list to store the fasta files
    fasta = []
    # Make an empty header
    header = ''
    # Make an empty string to store the sequence
    sequence = ''
    # Go through all lines
    for line in lines:
        # If the line starts with >
        if line.startswith('>'):
            # If this is not the first fasta sequence
            if header != '':
                # Add the previous fasta sequence to the list
                fasta.append([header, sequence])
                # Make a new header without the > symbol
                header = line[1:]
                # Reset the sequence
                sequence = ''
            # If this is the first fasta sequence
            else:
                # Make a new header without the > symbol
                header = line[1:]
        # If this is not a header
        else:
            # Make upper case and remove spaces
            line = re.sub(r'\s', '', line).upper()
            # Add the line to the sequence
            sequence += line
    # Add the last fasta sequence to the list
    fasta.append([header, sequence])

    return fasta


def shortest_superstring(sequences):
    """Returns a string containing all given strings

    Keyword arguments:
    sequences -- list of strings to be combined
    """

    # Start the superstring with the first of the sequences
    superstring = sequences[0]

    # Go through all the other sequences
    for seq in sequences[1:]:
        # Go through all possible overlap lengths
        for length in range(len(seq), 0, -1):
            # If the sequence is contained in the superstring, break
            if length == len(seq):
                if seq in superstring:
                    break
            # Find an overlap with the end of the new sequence
            kmer = seq[len(seq) - length:]
            # Find an overlap with the start of the superstring
            if superstring[:len(kmer)] == kmer:
                # Update the superstring to contain this sequence
                superstring = seq[:len(seq)-len(kmer)] + superstring
                break
            # Find an overlap with the start of the new sequence
            kmer = seq[0:length]
            # Find an overlap with the end of the superstring
            if superstring[len(superstring)-len(kmer):] == kmer:
                # Update the superstring to contain this sequence
                superstring = superstring + seq[len(kmer):]
                break

    return superstring

def main():
    """This code will be executed when called from the command line
    """

    # Step 1: Assign input to variables
    with open(argv[1]) as input_file:
        contents = input_file.read()

    # Step 2: Parse the fasta sequences
    name_seq_list = fasta_parser(contents)
    # obtain only the sequences
    seq_list = [item[1] for item in name_seq_list]

    # Step 3: Find the shortest superstring
    short_super = shortest_superstring(seq_list)
    print(short_super)

if __name__ == "__main__":
    main()
