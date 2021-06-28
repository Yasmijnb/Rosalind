#! /usr/env python3
"""
Author: Yasmijn Balder

Finds the N-glycosylation motif and gives start locations in proteins by their Uniprot ID
"""

from sys import argv
import urllib.request
import re

def get_fasta_from_Uniprot(UniprotID):
    """Returns a list with a name and protein fasta sequence from the UniprotID
    
    Keyword arguments:
    UniprotID --- a string, the UniprotID of a protein
    """

    # Make sure UniprotID is a string:
    UniprotID = str(UniprotID)

    # Create the uniprot url
    url = 'https://www.uniprot.org/uniprot/' + UniprotID + '.fasta'

    # Open the link
    with urllib.request.urlopen(url) as f:
        # Obtain the fasta sequence
        fasta = f.read().decode('utf-8')

    # Parse the fasta file
    sequence_list = fasta_parser(fasta)

    return sequence_list

def find_Nglycosylation_motif(protein_sequence):
    """Returns a list of positions where a motif starts in the given protein

    Keyword arguments:
    protein_sequence --- a string, a protein sequence
    """

    # The N-glycosylation motif:
    # N{P}[ST]{P}
    motiflength = 4

    # Initiate an empty list to save the places a motif starts
    positionlist = []
    
    # Make k-mers
    for aa in range(len(protein_sequence) - motiflength + 1):
        kmer = protein_sequence[aa:aa + motiflength]
        if kmer[0] == 'N' and kmer[1] != 'P' and kmer[3] != 'P':
            if kmer[2] == 'S' or kmer[2] == 'T':
                positionlist.append(aa+1)
    return positionlist

def fasta_parser(fasta_file):
    """Bla"""

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
            # Make sure there are no spaces and that the letters are in upper case
            line = re.sub(r'\s', '', line).upper()
            # Add the line to the sequence
            sequence+=line
    # Add the last fasta sequence to the list
    fasta.append([header, sequence])

    return fasta

def main():
    """This code will be executed when called from the command line
    """
# Step 1: assign input to variables
    with open(argv[1]) as f:
        proteins = []
        for line in f:
            proteins.append(line.strip())
            
# Step 2: Run code, print and save the output
    f = open("mprt_solution.txt", "a")
    for protein in proteins:
        sequence = get_fasta_from_Uniprot(protein)
        positions = find_Nglycosylation_motif(sequence[0][1])
        if positions != []:
            print(protein)
            f.write(protein)
            f.write('\n')
            print(" ".join(map(str, positions)))

            # Add the positions to the file
            f.write(" ".join(map(str, positions)))
            f.write('\n')
    # Close the file
    f.close()

if __name__ == "__main__":
    main()