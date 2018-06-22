import adjacency as adj

import numpy as np
import pandas as pd

ellista = open("ellista.txt", "r")

cells = []

for i in ellista.readlines():
    words = i.split(" ")
    cells.append(words[0])
    cells.append(words[1].split("\t")[0])

cells = np.array(cells)
unique_cells = np.unique(cells)
print(len(unique_cells))


master_matrix = {}
for c in unique_cells:
    a = adj.getAdjacencies(c)
    master_matrix[c] = a


for k, v in master_matrix.items():
    for cell in unique_cells:
        if cell not in v:
            v[cell] = 0

frame = pd.DataFrame(list(master_matrix.values()), index=list(master_matrix.keys()))
frame.to_csv("adjacency_matrix.csv")

ellista.close()
