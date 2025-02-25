from collections import defaultdict

# directed graph using adjacency list
class Graph:
    def __init__(self):
        # defaultdict to store graph
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def BFS(self, s):
        # mark all vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        
        # queue for BFS
        queue = []
        
        # mark source node as visited and enqueue
        queue.append(s)
        visited[s] = True
        
        while queue:
            # dequeue and print source node
            s = queue.pop(0)
            print(s, end=' ')
            
            # get all vertices adjacent to dequeued source node
            # if adjacent vertex not visited, mark visited and enqueue
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    
if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.BFS(2) # 2 0 3 1
