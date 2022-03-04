import networkx as nx
from networkx.algorithms.flow import edmonds_karp

G = nx.DiGraph()

edges_nr = int(input("introduceti numarul de muchii: "))

for x in range(edges_nr):
        G.add_edge(int(input("Introduceti primnul nod: ")),int(input("introduceti nodul adicent: ")), capacity = float(input("Introduceti ponderea: ")))
        x += 1

listnodes = list(G.nodes)

R = edmonds_karp(G, listnodes[0], listnodes[len(listnodes)-1])

x = int(input("introduceti nodul de start: "))
y = int(input("Introduceti nodul de finis: "))
while x and y not in G.nodes:
    print("nodurile nu fac parte din graf")
    x = int(input("introduceti nodul de start: "))
    y = int(input("Introduceti nodul de finis: "))

flow_value = nx.maximum_flow_value(G, x, y)
flow_value == R.graph["flow_value"]
print(flow_value)
