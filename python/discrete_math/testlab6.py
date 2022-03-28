import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt
import numpy as np
li= []
G = nx.read_edgelist("graph6.txt", nodetype=int, data=(('weight', int),))
nodes = G.nodes
all_edges = G.edges
for x in G.edges:
    li = G.edges[x]
    print(type(li))
    break




