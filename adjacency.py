import pandas as pd

def getAdjacencies(cellname, source="ellista.txt"):
    source = open(source, "r")
    adj = {}
    for i in source.readlines():
        words = i.split(" ")
        if cellname == words[0]:
            subs = words[1].split("\t")
            adj[subs[0]] = int(subs[1])

    source.close()

    return adj
