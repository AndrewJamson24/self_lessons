from collections import defaultdict

nodes = list(map(int,input("introduceti nodurule prin spatiu " ).split()))
all_edges = list(tuple(map(int,input().split())) for r in range(int(input('Numarul de muchii si perechile de muchii : '))))

class Graph:
        def __init__(self,Nodes):
            self.graph = defaultdict(list)
            self.nodes = Nodes
            self.adj_list = {}
            for node in self.nodes:
                self.adj_list[node] = []

        def add_edge(self,u,v):
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
            self.graph[u].append(v)
            self.graph[v].append(u)

        def adds_zero(self):
            for node in self.nodes:
                self.adj_list[node].append(str(0))

        def print_adj_list(self):
            for node in self.nodes:
                print(node,"->",self.adj_list[node])
        
        def DFSUtil(self, v, visited):
            visited.add(v)
            print(v, end=' ')
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    self.DFSUtil(neighbour, visited)
        def DFS(self, v):
            visited = set()
            self.DFSUtil(v, visited)
   
graph = Graph(nodes)
for u,v in all_edges:
    graph.add_edge(u,v)
graph.adds_zero()
print("Lista adiacenta")
graph.print_adj_list()
root = int(input("Introduceti nodul principal "))
print("Algoritmul de cautare in adancime cu nodul principal {} ".format(root))
graph.DFS(root)
