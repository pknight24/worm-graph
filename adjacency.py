import pandas as pd

def getAdjacencies(cellname, source="ellista.txt"):
    source = open(source, "r")
    adj = {}
    for i in source.readlines():
        words = i.split(" ")
        subs = words[1].split("\t")
        if cellname == words[0]:
            adj[subs[0]] = int(subs[1])
        elif cellname == subs[0]:
            adj[words[0]] = int(subs[1])

    source.close()

    return adj
