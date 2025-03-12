'''
Problem: Number of Islands

Given an 'm x n' 2D binary grid 'grid' which represents a map of '1's (land) and '0's
(water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 3
'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set() # set to explore islands
        count = 0 # island count
        
        # DFS to explore islands
        def dfs(r, c):
            # edge cases (out of bounds, water, already visited)
            if (r < 0 or r >= rows or c < 0 or c >= cols \
                or grid[r][c] == '0' or (r, c) in visited):
                return
            
            visited.add((r, c)) # visit island
            
            # explore all four directions
            dfs(r - 1, c) # up
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right
            
        for r in range(rows):
            for c in range(cols):
                # visit island and add to count
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
                    
        return count
        
