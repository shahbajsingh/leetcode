from collections import defaultdict

class TopologicalSort:
    @staticmethod
    def topological_sort(n, edges):
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
            
        stack = [i for i in range(n) if in_degree[i] == 0]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)
                    
        return result if len(result) == n else []
