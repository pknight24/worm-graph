import adjacency as adj
import graphbuilder as gb

import numpy as np
import pandas as pd
import sys
import argparse

ellista = open("ellista.txt", "r")

cells = []

for i in ellista.readlines():
    words = i.split(" ")
    cells.append(words[0])

cells = np.array(cells)
unique_cells = np.unique(cells)


parser = argparse.ArgumentParser(description="Query the C. elegans connectome")
parser.add_argument("ROOT", help="The starting neuron for building graphs or finding connections.")
parser.add_argument("-g", "--graph", action="store_true", help="Specify whether you want to see a graph of the query.")
parser.add_argument("-t", "--to", action="append", help="Specify any neuron(s) that you want to query to from ROOT.")
parser.add_argument("-w","--weighted", action="store_true", help="Specify whether you wanted to represented the number of connections between pairs of neurons in a graph as edge darkness")

args = parser.parse_args()
root = args.ROOT
ad = adj.getAdjacencies(root)
graph = args.graph
to = args.to
weighted = args.weighted

if not graph:
    ad = pd.Series(ad)
    if not to:
        print(ad)
    else:
        wanted = ad.filter(items=to)
        print(wanted)
else:
    if not to:
        g = gb.buildGraph(root, ad)
        gb.display(g,weighted)
    else:
        wanted = {}
        for k,v in ad.items():
            if k in to:
                wanted[k] = v
        g = gb.buildGraph(root, wanted)
        gb.display(g, weighted)


ellista.close()
