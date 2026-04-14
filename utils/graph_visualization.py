import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(sites):
    G = nx.DiGraph()

    for site in sites:
        for src, targets in site.get_graph().items():
            for dst in targets:
                G.add_edge(f"P{src}", f"P{dst}")

    plt.figure()
    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        node_size=2000,
        font_size=10
    )

    return plt