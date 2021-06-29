#! /usr/env python3
"""
Author: Yasmijn Balder

Rosalind problem: revp
Finds reverse palindromes of 4-12 nucleotides in a given sequence.
Prints the position and length of every reverse palindromes as integers \
    separated by spaces, each on a new line
"""

import re
from sys import argv


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
    # Make an empty string to store the sequence
    sequence = ''
    # Go through all lines
    for line in lines:
        # If the line starts with >
        if line.startswith('>'):
            # If this is not the first fasta sequence
            if len(fasta) > 0:
                # Add the previous fasta sequence to the list
                fasta.append([header, sequence])
                # Make a new header
                header = line
                # Reset the sequence
                sequence = ''
            # If this is the first fasta sequence
            else:
                # Make a new header
                header = line
        # If this is not a header
        else:
            # Make upper case and remove spaces
            line = re.sub(r'\s', '', line).upper()
            # Add the line to the sequence
            sequence += line
    # Add the last fasta sequence to the list
    fasta.append([header, sequence])

    return fasta


def reverse_complement(dna_sequence):
    """Returns the reverse complement of a given dna sequence
    """

    # Make sure dna_sequence is upper case
    dna_sequence = dna_sequence.upper()

    # Create dictionary of complements:
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    # Obtain the complement of the dna sequence
    complement = ''
    for nucleotide in dna_sequence:
        complement += complements[nucleotide]

    # Reverse the complement
    rev_complement = complement[::-1]

    return rev_complement


def find_reverse_palindrome(dna_sequnence):
    """Returns"""

    # Make sure dna_sequence is upper case
    dna_sequnence = dna_sequnence.upper()

    # Initiate a list to store the palindromes
    palindromes = []

    # Make k-mers from 4 to 12 nucleotides
    for length in range(4, 13, 2):
        # Go through all start positions
        for nucleotide in range(len(dna_sequnence) - length + 1):
            # Make a kmer of the given length
            kmer = dna_sequnence[nucleotide: nucleotide + length]
            # Save the first half of the kmer
            first = kmer[0:int(length / 2)]
            # Obtain the reverse complement of the last half of the kmer
            last = reverse_complement(kmer[int(length / 2): length])
            # Palindromes have equal first as the revcom of the last
            if first == last:
                # The start position needs to be increased by one (python 0)
                position = nucleotide + 1
                # Add the palindrome start positions and length to the list
                palindromes.append([position, length])

    return palindromes


def main():
    """This code will be executed when called from the command line
    """

    # Step 1: assign input to variables
    with open(argv[1]) as f:
        input = ""
        for line in f:
            input += line.strip()
            input += '\n'
    fasta = fasta_parser(input)

    # Step 2: Run code, print and save the output
    pals_and_positions = find_reverse_palindrome(fasta[0][1])
    for hit in pals_and_positions:
        print(' '.join(map(str, hit)))


if __name__ == "__main__":
    main()
