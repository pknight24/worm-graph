import adjacency as adj
import graphbuilder as gb

import numpy as np
import pandas as pd
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
    
    args = sys.argv[1:]
    if (args[0] == "-g" or args[0] == "--graph"):
        root = args[1]
        ad = adj.getAdjacencies(root)
        graph = gb.buildGraph(root, ad)
        gb.display(graph)

    else:
        root = args[0]
        ad = adj.getAdjacencies(root)
        if (len(sys.argv) == 3):
            key = args[1]
            if key in ad:
                print(ad[key])
            else:
                print(0)
        else:
            print(pd.Series(ad))

ellista.close()
