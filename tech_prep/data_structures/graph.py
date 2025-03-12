from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # adjacency list representation
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        '''Add (undirected) edge to graph.'''
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def bfs(self, start):
        '''Perform BFS traversal from a starting node.'''
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                queue.extend(self.graph[node])
                
    def dfs(self, start, visited=None):
        '''Perform DFS traversal from a starting node.'''
        if visited is None:
            visited = set()
            
        if start in visited:
            return
        print(start, end=' ')
        visited.add(start)
        
        for neighbor in self.graph[start]:
            self.dfs(neighbor, visited)
