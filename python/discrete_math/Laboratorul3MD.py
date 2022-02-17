from collections import defaultdict

nodes = list(map(int,input("introduceti nodurule prin spatiu " ).split()))
all_edges = list(tuple(map(int,input().split())) for r in range(int(input('Numarul de muchii si perechile de muchii : '))))

class Graph:
        def __init__(self,Nodes):
            self.nodes = Nodes
            self.adj_list = {}
            self.graph = defaultdict(list)
            for node in self.nodes:
                self.adj_list[node] = []

        def add_edge(self,u,v):
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
            self.graph[u].append(v)
            self.graph[v].append(u)


        def adds_zero(self):
            for node in self.nodes:
                self.adj_list[node].append("0")

        def print_adj_list(self):
            for node in self.nodes:
                print(node,"->",self.adj_list[node])
        
        def BFS(self, s):
            visited = [False] * (max(self.graph) + 1)
            queue = []
            queue.append(s)
            visited[s] = True
            while queue:
                s = queue.pop(0)
                print (s, end = " ")
                for i in self.graph[s]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
   
graph = Graph(nodes)
for u,v in all_edges:
    graph.add_edge(u,v)
graph.adds_zero()
print("lista de adiacenta")
graph.print_adj_list()

root = int(input("Introduceti nodul principal "))
print("Algoritmul de cautare in largime cu nodul principal {} ".format(root))
graph.BFS(root)
