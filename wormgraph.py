import adjacency as adj
import graphbuilder as gb

import numpy as np
import pandas as pd
import sys
import argparse
import re

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

args = parser.parse_args()
root = args.ROOT
ad = adj.getAdjacencies(root)
graph = args.graph
to = args.to

if to:
    wanted = {}
    for k, v in ad.items():
        for t in to:
            if (re.search(t, k)):
                 wanted[k] = v
else:
    wanted = ad

if not graph:
    print(pd.Series(wanted))
else:
    g = gb.buildGraph(root, wanted)
    gb.display(g)

ellista.close()
