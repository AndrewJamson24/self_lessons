import networkx as nx 
import sys

nodes = list(map(int,input("introduceti nodurule prin spatiu " ).split()))
edges_nr = int(input("introduceti numarul de muchii: "))

G = nx.Graph()

for x in range(edges_nr):
    G.add_edge(int(input("Introduceti primnul nod: ")),int(input("introduceti nodul adicent: ")),weight = int(input("Introduceti ponderea: ")))
    x += 1

length = dict(nx.all_pairs_bellman_ford_path_length(G))

while True:
    x = int(input("introduceti nodul de start: "))
    y = int(input("Introduceti nodul de finis: "))

    print("drumul minim din {} in {} ".format(x,y))
    print(f" {x}-> {y}: {length[x][y]}")
    r = input("Doriti alte valori de start si finis? : ").capitalize()
    if r == "Da":
        pass
    else :
        sys.exit()
 
#Bellman-Ford algortims shortest path in graph
