import networkx as nx


G = nx.DiGraph()

edges_nr = int(input("introduceti numarul de muchii: "))

for x in range(edges_nr):
        G.add_edge(int(input("Introduceti primnul nod: ")),int(input("introduceti nodul adicent: ")), capacity = float(input("Introduceti capacitatea: ")))
        x += 1

x = int(input("introduceti nodul de start: "))
y = int(input("Introduceti nodul de finis: "))
while x and y not in G.nodes:
    print("nodurile nu fac parte din graf")
    x = int(input("introduceti nodul de start: "))
    y = int(input("Introduceti nodul de finis: "))

flow_value = nx.maximum_flow_value(G, x, y)
print(flow_value)
