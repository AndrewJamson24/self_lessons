import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph

G = nx.read_edgelist("graph6.txt", nodetype=int, data=(("weight", int),))
nodes = G.nodes
all_edges = G.edges
pos=nx.circular_layout(G) 
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

def Adjacency_matrix():
    print("Matricea de adiacenta")

    G.add_nodes_from(nodes)
    G.add_edges_from(all_edges)
    A = np.array(nx.adjacency_matrix(G,nodelist=sorted(G.nodes()),weight="weight").todense())
    print(A)

def Graph_list():
    class Graph:
        def __init__(self,Nodes):
            self.nodes = Nodes
            self.adj_list = {}
            for node in self.nodes:
                self.adj_list[node] = []

        def add_edge(self,u,v):
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)


        def adds_zero(self):
            for node in self.nodes:
                self.adj_list[node].append("0")

        def print_adj_list(self):
            for node in self.nodes:
                print(node,"->",self.adj_list[node])
    print("Lista de adiacenta")
   
    graph = Graph(nodes)
    for u,v in all_edges:
        graph.add_edge(u,v)
    graph.adds_zero()

    graph.print_adj_list()
    


def MST():
    mst = tree.minimum_spanning_edges(G,weight="weight", algorithm="prim", data=False)
    edgelist = list(mst)
    print(edgelist)
    sorted(sorted(e) for e in edgelist)
    H = nx.DiGraph()
    H.add_edges_from(edgelist)
    pos=nx.circular_layout(H) 
    nx.draw_networkx(H,pos)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(H,pos,edge_labels=labels)
    plt.show()


def Menu():
    while True :
        print("\n*******Meniul principal*******")

        choice = input("""
        
        1: Graful de acoperire
        2: Matricea 
        3: Lista
        0: Iesire

        Alegeti o optiunea:   """)

        if choice == "1":
            MST()
        elif choice == "2":
            Adjacency_matrix()
        elif choice =="3":
            Graph_list()
        elif choice == "0":
            quit()
        else :
            print("alegerea nu este din meniu")

Menu()

#To be used with file graph6.txt , its getting data from there
