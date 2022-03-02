#! /usr/env python3
"""
Author: Yasmijn Balder

Rosalind problem: corr
This function returns the all corrections for single nucleotide sequencing
errors in the form "[old read]->[new read]".
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

def correct_single_errors(sequence_list):
    """Returns a list with correct sequences. Contains all sequences with
    changes for single error corrections.

    Keyword arguments:
    sequence_list -- a list of strings
    """

    # Create an empty list to store the correct sequences
    correct_sequences = []

    # Go through all the sequences
    for seq in sequence_list:
        # Find the reverse complement to use later
        revcom = reverse_complement(seq)
        # If the sequence is correct, it appears in at least twice
        if sequence_list.count(seq) > 1:
            correct_sequences.append(seq)
        # The sequence could appear as the reverse compliment
        elif sequence_list.count(revcom) > 0:
            correct_sequences.append(seq)
        # Otherwise the sequence contains a sequencing error
        else:
            # Find a sequence with a hamming distance of 1
            for other_seq in sequence_list:
                # Find the reverse complement of the other sequence
                other_revcom = reverse_complement(other_seq)
                if hamming_distance(seq, other_seq) == 1:
                    # Make sure the match is a correct sequence
                    if sequence_list.count(other_seq) > 1 or sequence_list.count(other_revcom) > 0:
                        correct_sequences.append(other_seq)
                        break
            # Find a rev com sequence with a hamming distance of 1
                elif hamming_distance(revcom, other_seq) == 1:
                    # Make sure the match is a correct sequence
                    if sequence_list.count(other_seq) > 1 or sequence_list.count(other_revcom) > 0:
                        correct_sequences.append(other_revcom)
                        break

    return correct_sequences

def hamming_distance(seq1, seq2):
    """Returns the hamming distance between two sequences

    Keyword arguments:
    seq1 -- a string
    seq2 -- a string of equal size
    """

    # Initialy the hamming distance at 0
    hamm_dist = 0

    # Go through each nucleotide
    for base in range(len(seq1)):
        # See if the nucleotide is different in both sequences
        if seq1[base] != seq2[base]:
            # Increase the hamming distance with 1
            hamm_dist += 1

    return hamm_dist

def reverse_complement(sequence):
    """Returns the reverse complement of the given dna sequence in upper case

    Keyword arguments:
    sequence -- a string
    """

    # Make sure the sequence is in upper case
    sequence = sequence.upper()

    # Create a dictionary with the complement of each nucleotide
    complement_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

    # Create the complement of the sequence
    complement = "".join(complement_dict[base] for base in sequence)

    # Create the reverse of the complement
    rev_comp = complement[::-1]

    return rev_comp

def format_error_corrections(old_seqlist, new_seqlist):
    """Returns
    """

    for seq in range(len(old_seqlist)):
        if old_seqlist[seq] != new_seqlist[seq]:
            print(old_seqlist[seq], '->', new_seqlist[seq], sep='')

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

    # Step 3: Find the corrections for single nucleotide sequencing errors
    fixed = correct_single_errors(seq_list)
    format_error_corrections(seq_list, fixed)

if __name__ == "__main__":
    main()
