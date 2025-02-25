from collections import defaultdict

# directed graph using adjacency list
class Graph:
    def __init__(self):
        # defaultdict to store graph
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    # helper function
    def visit(self, v, visited):
        # mark current node as visited
        visited.add(v)
        print(v, end=' ')
        
        # visit adjacent vertices recursively
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.visit(neighbor, visited)
                
    def DFS(self, v):
        visited = set()
        self.visit(v, visited)
        
if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    g.DFS(2) # 2 0 1 3