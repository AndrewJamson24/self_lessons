from typing import Any
import networkx as nx 
import matplotlib.pyplot as plt

edges_nr = int(input("introduceti numarul de muchii: "))

G = nx.DiGraph()

path_l_s = ""

while path_l_s != "maxim" or path_l_s != "minim":
    print("Introduceti dupa modelul din paranteze (maxim / minim)")
    path_l_s = input("Cel mai lung sau cel mai scurt drum?(maxim/minim): ").lower()
    if path_l_s == "maxim":
        for x in range(edges_nr):
            G.add_edge(int(input("Introduceti primnul nod: ")),int(input("introduceti nodul adicent: ")), weight = -abs(int(input("Introduceti ponderea: "))))
            x += 1
        length = dict(nx.all_pairs_bellman_ford_path_length(G))
        pos = nx.circular_layout(G)
        nx.draw_networkx(G, pos)
        labels = nx.get_edge_attributes(G, ('weight'))
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
        break
 
    elif path_l_s == "minim":
        for x in range(edges_nr):
            G.add_edge(int(input("Introduceti primul nod: ")),int(input("introduceti nodul adicent: ")), weight = int(input("Introduceti ponderea: ")))
            x += 1
        length = dict(nx.all_pairs_bellman_ford_path_length(G))
        pos = nx.circular_layout(G)
        nx.draw_networkx(G, pos)
        labels = nx.get_edge_attributes(G, ('weight'))
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
        break


x = int(input("nodul de start: "))
y = int(input("ultimul nod: "))


if path_l_s == "maxim":
    print("drumul maxim din {} in {} ".format(x,y))
    print(f" {x}-> {y}: {abs(length[x][y])}")
    pathnodes = dict(nx.all_pairs_bellman_ford_path(G))
    print(f"Drumul cel mai lung drum este \n{pathnodes[x][y]}")
    

else:
    print("drumul minim din {} in {} ".format(x,y))
    print(f" {x}-> {y}: {length[x][y]}")
    print("Cele mai scurte drumuri")
    print([p for p in nx.all_shortest_paths(G,source=x,target=y,weight='weight')])

    

