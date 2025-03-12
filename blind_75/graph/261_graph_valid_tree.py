'''
Problem: Graph Valid Tree

Given 'n' nodes labeled from '0' to 'n-1' and a list of undirected edges (each edge 
is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n=5, edges=[[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:

Input: n=5, edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Note: you can assume that no duplicate edge will appear in 'edges'. Since all edges 
are undirected, '[0,1]' is the same as '[1,0]' and thus will not appear together in 'edges'.
'''
from typing import List

class Solution:
    def validTree(self, num_nodes: int, edges: List[List[int]]) -> bool:
        # if number of edges and number of nodes - 1 do not match, not a tree
        if len(edges) != num_nodes - 1:
            return False
        
        # build adjacency list for graph
        graph = {i: [] for i in range(num_nodes)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
            # use DFS to check connectivity
            
            visited = set()
            
            def dfs(node, parent):
                if node in visited: # cycle detected
                    return False
                
                visited.add(node)
                
                for neighbor in graph[node]:
                    if neighbor == parent: # skip edge back to parent
                        continue
                    if not dfs(neighbor, node): # recursively visit neighbors
                        return False
                    
                return True
            
        # start DFS from node 0
        return dfs(0, -1) and \
            len(visited) == num_nodes # check if all nodes visited and no cycles