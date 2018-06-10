def buildGraph(root, adj):
    import networkx as nx
    import adjacency as ad

    G = nx.Graph()
    G.add_node(root)
    for key in adj:
        key_adjacencies = ad.getAdjacencies(key)
        G.add_node(key)
        e = (root, key)
        G.add_edge(*e)
        for i in key_adjacencies:
            if i in adj:
                ee = (key, i)
                G.add_edge(*ee)
    return G

def display(g):
    import networkx as nx
    import matplotlib.pyplot as plt

    nx.draw(g, with_labels=True, edge_color = "#b4abab", node_color="#01a1ff", width=2)
    plt.show()
