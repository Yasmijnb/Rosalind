#! /usr/env python3
"""
Author: Yasmijn Balder

Rosalind problem: cc
This function returns the number of connected components in a graph from edge
list format.
"""

from sys import argv

def depth_first_search(edgelist, nodes):
    """Returns a list with the number of the component each node is in

    Keyword arguments:
    edgelist -- list of lists, of two nodes (int) which are connected
    nodes -- total number of nodes (int)
    """

    # Make a list for the component number of each node
    ccnum = [0] * nodes
    # Start with zero components
    current_component = 0
    # Make a list for if each node has been visited yet
    visited = [False] * nodes
    # Go by each node
    for node in range(1, nodes):
        # Go only by nodes that have not been visited yet
        if visited[(node - 1)] == False:
            # Increase the number of components
            current_component += 1
            # Explore this node
            explore(edgelist, node, visited, current_component, ccnum)

    return ccnum

def explore(edgelist, node, visited, current_component, ccnum):
    """Explores the neighbours of each node

    Keyword arguments:
    edgelist -- list of lists, of two nodes (int) which are connected
    nodes -- total number of nodes (int)
    visited -- list of boolean whether a node has been explored
    current_component -- the number of the component being explored (int)
    ccnum -- list of the component (int) in which each node is
    """

    # This node is now being explored, so change visited to true
    visited[(node - 1)] = True
    # Annotate this node with the component in which it was found
    ccnum[(node - 1)] = current_component

    # Go through each edge in the edgelist
    for edge in edgelist:
        # Only look at edges from this node
        if edge[0] == node:
            # Find the connected nodes that have not been explored yet
            if visited[(edge[1]-1)] == False:
                # Explore the connected node
                explore(edgelist, edge[1], visited, current_component, ccnum)

def main():
    """This code will be executed when called from the command line
    """
    # Step 1: Assign input to variables
    nodes = 0
    edgelist = []
    with open(argv[1]) as input_file:
        for line in input_file:
            items = line.split()
            if nodes == 0:
                nodes = int(items[0])
            else:
                edgelist.append([int(items[0]), int(items[1])])

    # Step 2: Obtain the number of component each node is in
    number_of_cc = depth_first_search(edgelist, nodes)

    # Step 3: Print the total number of components
    print(max(number_of_cc))




if __name__ == "__main__":
    main()
