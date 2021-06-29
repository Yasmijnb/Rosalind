#! /usr/env python3
"""
Author: Yasmijn Balder

Rosalind problem: lcsm
Finds the longest common substring of given sequences
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


def longest_common_substrings(fasta_list):
    """Returns a list of the longest common substring(s) found in the given
    sequences

    Keyword arguments:
    fasta_list -- list of lists with a sequence name and sequence
    """

    # Obtain all sequences
    sequence_list = [seq[1] for seq in fasta_list]

    # The maximum length of the substring is equal to the shortest given seq
    maxlength = min([len(seq) for seq in sequence_list])

    # Initiate an empty dictionary for the kmers and occurences
    kmer_dict = {}
    # Go through all sequences
    for number, seq in enumerate(sequence_list):
        # Go through all possible substring lengths
        for length in range(2, maxlength + 1):
            # Go through all possible start positions
            for start in range(len(seq) - length + 1):
                # Create a kmer
                kmer = seq[start: (start + length)]
                # If the kmer found before
                if kmer in kmer_dict:
                    # Increase the occurence with one
                    kmer_dict[kmer] += 1
                # Only create a dictionary entry during the first sequence
                elif number == 0:
                    # Add the kmer to the dictionary with occurrence 1
                    kmer_dict[kmer] = 1

    # The number of sequences
    tot_seq = len(sequence_list)
    # Collect all kmers that occur in all sequences
    common_list = [kmer for kmer, occ in kmer_dict.items() if occ == tot_seq]
    # Create a dictionary with the kmers and their lengths
    len_dict = {kmer: len(kmer) for kmer in common_list}
    # Get a list with only the longest kmers
    longest = max(len_dict.values())
    longest_commons = [kmer for kmer, l in len_dict.items() if l == longest]

    return longest_commons


def main():
    """This code will be executed when called from the command line
    """

    # Step 1: Assign input to variables
    with open(argv[1]) as f:
        contents = f.read()

    # Step 2: Parse the fasta sequences
    seq_list = fasta_parser(contents)

    # Step 3: Find the longest common substrings
    long_list = longest_common_substrings(seq_list)

    # Step 4: Return one of the longest common substrings
    print(long_list[0])


if __name__ == "__main__":
    main()
