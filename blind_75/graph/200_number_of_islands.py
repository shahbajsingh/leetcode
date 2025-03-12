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
        # edge case
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0]) # grid dimensions
        visited = set() # track visited cells
        count = 0 # island count
        
        # DFS
        def dfs(r, c):
            # base case (out of bounds, water, or already visited)
            if (r < 0 or r >= rows or c < 0 or c >= cols or \
                grid[r][c] == '0' or (r, c) in visited):
                return
            
            visited.add((r, c)) # mark visited
            
            # explore all four directions
            dfs(r - 1, c) # up
            dfs(r + 1, c) # down
            dfs(r, c - 1) # left
            dfs(r, c + 1) # right
            
        for r in range(rows):
            for c in range(cols):
                # if cell is land and not visited, explore and increment island count
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c) # explore island
                    count += 1
                    
        return count
