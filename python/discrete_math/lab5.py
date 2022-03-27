import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

G = nx.DiGraph()

G = nx.read_edgelist("graph5.txt", nodetype=int, data=(("capacity", float),))
        
while True:
    x = int(input("introduceti nodul de start: "))
    y = int(input("Introduceti nodul de finis: "))
    while x and y not in G.nodes:
        print("nodurile nu fac parte din graf")
        x = int(input("introduceti nodul de start: "))
        y = int(input("Introduceti nodul de finis: "))

    flow_value = nx.maximum_flow(G, x, y)
    print("Capacitatea maxima pe graf este {}".format(flow_value))
    
    break

#Reads from a file in the same directory
