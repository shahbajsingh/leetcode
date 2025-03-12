'''
Problem: Number of Connected Components in an Undirected Graph

Given 'n' nodes labeled from '0' to 'n-1' and a list of undirected edges (each 
edge is a pair of nodes), write a function to find the number of connected 
components in an undirected graph.

Example 1:

Input: n=5, edges=[[0,1],[1,2],[3,4]]
        0           3
        |           |
        1 --- 2     4
Output: 2

Example 2:

Input: n=5, edges=[[0,1],[1,2],[2,3],[3,4]]
        0           4
        |           |
        1 --- 2 --- 3
Output: 1

Note:

You can assume that no duplicate edges will appear in 'edges'. Since all edges are 
undirected, '[0,1]' is the same as '[1,0]' and thus will not appear together in 
'edges'.
'''
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set() # track visited nodes
        comps = 0 # components 
        
        # DFS to explore component
        def dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            
        # count components by triggering DFS for unvisited nodes
        for node in range(n):
            if node not in visited:
                comps += 1
                dfs(node)
                
        return comps