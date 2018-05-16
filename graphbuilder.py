def buildGraph(root, adj):
    import networkx as nx

    G = nx.Graph()
    G.add_node(root)
    for key in adj:
        G.add_node(key)
        e = (root, key)
        G.add_edge(*e)
    return G

def display(g):
    import networkx as nx
    import matplotlib.pyplot as plt

    nx.draw(g, with_labels=True)
    plt.show()

