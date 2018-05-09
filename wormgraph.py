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
    print("Usage:\n\twormgraph <CELLCLASS> <CELLCLASS>\n\tIf only one cell class is given, all connections for the given cell class will be returned.")
else:
    ad = adj.getAdjacencies(sys.argv[1])
    if (len(sys.argv) == 3):
        print(ad[sys.argv[2]])
    else:
        print(ad)

ellista.close()
