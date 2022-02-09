from ftplib import all_errors
from re import search
import networkx as nx
import numpy as np
import sys
global save_file 
save_file = bool(eval("False"))

def NEO():
    global nodes
    global all_edges
    global is_oriented
    is_oriented = eval(input("Graful este orientat? (True/False) ").capitalize())
    bool(is_oriented)
    nodes = list(map(int,input("introduceti nodurule prin spatiu " ).split()))
    all_edges = list(tuple(map(int,input().split())) for r in range(int(input('Numarul de muchii si perechile de muchii : '))))
    for u,v in all_edges:
        if u and v not in nodes:
            sys.exit('Eroare la introducerea muchiilor ')
    
def Graph_list():
    class Graph:
        def __init__(self,Nodes):
            self.nodes = Nodes
            self.adj_list = {}
            for node in self.nodes:
                self.adj_list[node] = []

        def add_edge(self,u,v):
            self.adj_list[u].append(v)
            if not is_oriented:
                self.adj_list[v].append(u)


        def adds_zero(self):
            for node in self.nodes:
                self.adj_list[node].append("0")

        def print_adj_list(self):
            for node in self.nodes:
                print(node,"->",self.adj_list[node])
    if save_file:

        graph = Graph(nodes)
        for u,v in all_edges:
            graph.add_edge(u,v)
        graph.adds_zero()
        with open("Laboratorul_test.txt", 'w') as sys.stdout:
            print(graph.print_adj_list())
    else :
        graph = Graph(nodes)
        for u,v in all_edges:
            graph.add_edge(u,v)
        graph.adds_zero()
        graph.print_adj_list()

    

def Adjacency_Matrix():
    if is_oriented:
        G = nx.MultiDiGraph()
    else :
        G = nx.MultiGraph()

    G.add_nodes_from(nodes)
    G.add_edges_from(all_edges)
    A = np.array(nx.adjacency_matrix(G,nodelist=sorted(G.nodes()),weight="weight").todense())
    print(A)

    
def Incidence_matrix():
    if not is_oriented :
        print("Matricea nu este orientata si nu este posibila operatia")
        menu()
    else :
        H = nx.MultiDiGraph()
        H.add_nodes_from(nodes)
        H.add_edges_from(all_edges)
        inc_matrix = np.array(nx.incidence_matrix(H,oriented=True,weight="weight").todense())
        inc_matrix_transpose = inc_matrix.transpose()
        print(inc_matrix_transpose)

    
def remove_node():
    x = int(input("Ce nod doriti sa stergeti? "))
    nodes.pop(nodes.index(x))

def remove_edges():
    a = int(input("primul nod al muchiei : "))
    b = int(input("al doilea nod la muchiei : "))
    search_list = [i for (i, a_tuple) in enumerate(all_edges) if a_tuple[0]== a and a_tuple[1]== b]
    v = search_list[0]
    all_edges.pop(v)

def add_node():
    new_node = int(input("ce nod doriti sa adaugati? "))
    if new_node in nodes :
        print("Nodul deja este in lista")
    else:
        nodes.append(new_node)    

def add_edge():
    node1 = [int(input("primul nod al mnuchiei"))]
    node2 = [int(input("al doilea nod al mnuchiei"))]
    new_edge = tuple(node1 + node2)
    if  new_edge in all_edges:
        print("muchia exista deja")
    else:
        all_edges.append(new_edge)




def menu():
    while True :
        print("\n*******Meniul principal*******")

        choice = input("""
        
        1: Datele pentru graf
        2: Lista adiacenta
        3: Matricea de incidenta
        4: Matricea de adiacenta
        5: Stergerea unui nod
        6: Stergerea unei muchii
        7: Adaugarea unui nod
        8: Adaugarea unei muchii
        9: Salvarea list_ad in fiesier aparte
        0: Iesirea din meniu

        Alegeti o optiunea:   """)

        if choice == "1":
            NEO()
        elif choice == "2":
            Graph_list()
        elif choice == "3":
            Incidence_matrix()
        elif choice =="4": 
            Adjacency_Matrix()
        elif choice =="5": 
            remove_node()
        elif choice =="6":
            remove_edges()
        elif choice =="7":
            add_node()
        elif choice =="8":
            add_edge()
        elif choice =="9": 
            save_file = True
            Graph_list()    
        elif choice == "0":
            quit()
        else :
            print("alegerea nu este din meniu")
            
menu()
