#! /usr/env python3
"""
Author: Yasmijn Balder

Rosalind problem: orf
This function returns every distinct candidate protein string that can be
translated from ORFs.
"""

from sys import argv
import re
from threading import currentThread

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

def find_open_reading_frames(dna_sequence):
    """Returns a list of open reading frames
    """

    # Create an empty list to store all the orfs
    orfs = []
    # Create an empty string to append the current orf
    current_orf = ''

    start_codon = 'ATG'
    stop_codons = ['TAA', 'TAG', 'TGA']

    # Find the three reading frames in the forward rna sequence
    for startbase in range(0,len(dna_sequence) - 2):
        codon = dna_sequence[startbase:startbase + 3]
        if codon == start_codon:
            current_orf = codon
        elif codon in stop_codons and current_orf:
            # Add this orf to the orfs list
            orfs.append(current_orf)
            # Restart the orf by emptying the current orf list
            current_orf = ''
        elif current_orf:
            current_orf += codon

    revcomp = reverse_complement(dna_sequence)
    # Find the three reading frames in the reverse complement
    for startbase in range(0,len(dna_sequence) - 2):
        codon = dna_sequence[startbase:startbase + 3]
        if codon == start_codon:
            current_orf = codon
        elif codon in stop_codons and current_orf:
            # Add this orf to the orfs list
            orfs.append(current_orf)
            # Restart the orf by emptying the current orf list
            current_orf = ''
        elif current_orf:
            current_orf += codon

    return orfs

def transcripe_dna(dna_sequence):
    """Returns the given string with U instead of T in upper case

    Keyword arguments:
    dna_sequence -- a string
    """

    # Make sure the dna sequence is in upper case
    dna_sequence = dna_sequence.upper()

    # Replace each T in the dna sequence with a U
    rna_sequence = dna_sequence.replace('T', 'U')

    return rna_sequence

def translate_rna(rna_sequence):
    """Returns a string of amino acids

    Keyword arguments:
    rna_sequence -- a string consisting of U, A, C, and G
    """

    # Make sure the rna sequence is in upper case
    rna_sequence = rna_sequence.upper()

    # Create an empty string to store the protein sequence
    protein_seq = ''

    # Create a dictionary with codons and their corresponding amino acids
    translation_dict = {'UUU':'F','CUU':'L','AUU':'I','GUU':'V','UUC':'F',
    'CUC':'L','AUC':'I','GUC':'V','UUA':'L','CUA':'L','AUA':'I','GUA':'V',
    'UUG':'L','CUG':'L','AUG':'M','GUG':'V','UCU':'S','CCU':'P','ACU':'T',
    'GCU':'A','UCC':'S','CCC':'P','ACC':'T','GCC':'A','UCA':'S','CCA':'P',
    'ACA':'T','GCA':'A','UCG':'S','CCG':'P','ACG':'T','GCG':'A','UAU':'Y',
    'CAU':'H','AAU':'N','GAU':'D','UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
    'UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E','UAG':'Stop','CAG':'Q',
    'AAG':'K','GAG':'E','UGU':'C','CGU':'R','AGU':'S','GGU':'G','UGC':'C',
    'CGC':'R','AGC':'S','GGC':'G','UGA':'Stop','CGA':'R','AGA':'R','GGA':'G',
    'UGG':'W','CGG':'R','AGG':'R','GGG':'G'}

    # Go through each codon
    for base in range(0, len(rna_sequence), 3):
        codon = rna_sequence[base:base+3]
        # Find the corresponding amino acids and append it to the protein seq
        protein_seq += translation_dict[codon]

    return protein_seq

def main():
    """This code will be executed when called from the command line
    """

    # Step 1: Assign input to variables
    with open(argv[1]) as input_file:
        contents = input_file.read()

    # Step 2: Parse the fasta sequences
    name_seq_list = fasta_parser(contents)
    # obtain only the sequence
    sequence = [item[1] for item in name_seq_list][0]

    print(sequence)

    # Step 3: Find the ORFs
    orfs = find_open_reading_frames(sequence)
    print(orfs)

    # Step 4: Translate the ORFs to proteins
    for orf in orfs:
        print(orf)
        rna = transcripe_dna(orf)
        print(translate_rna(rna))

if __name__ == "__main__":
    main()
