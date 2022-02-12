from collections import defaultdict
 
lenght = int(input("introduceti numarul de muchii din gaf "))
root = int(input("Introduceti nodul principal "))

class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)
 
# Driver code
 
 
# Create a graph given
# in the above diagram
g = Graph()
for x in range(0,lenght):
    i = int(input("Introduceti primul nod: "))
    q = int(input("Introduceti nodul conex cu primul: "))
    g.addEdge(i,q)
    x += 1    
 
print("Following is DFS from (starting from vertex {} )".format(root))
g.DFS(root)
