import adjacency as adj

import numpy as np
import pandas as pd
import networkx as nx
import sys



ellista = open("ellista.txt", "r")

cells = []

for i in ellista.readlines():
    words = i.split(" ")
    cells.append(words[0])

cells = np.array(cells)
unique_cells = np.unique(cells)

if (len(sys.argv) < 2):
    print("Usage:\n\twormgraph <NEURON> <NEURON>\n\tIf only one neuron is given, all connections for the given neuron will be returned.")
else:
    ad = adj.getAdjacencies(sys.argv[1])
    if (len(sys.argv) == 3):
        key = sys.argv[2]
        if key in ad:
            print(ad[key])
        else:
            print(0)
    else:
        print(pd.Series(ad))

ellista.close()
