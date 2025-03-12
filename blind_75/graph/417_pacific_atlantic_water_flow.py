'''
Problem: Pacific Atlantic Water Flow

There is an 'm x n' rectangular island that borders both the Pacific Ocean and 
Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the 
Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an 'm x n' 
integer matrix 'heights' where 'heights[r][c]' represents the height above sea 
level of the cell at coordinate (r,c).

The island receives a lot of rain, and the rain water can flow to neighboring cells 
directly north, south, east, and west if the neighboring cell's height is less than 
or equal to the current cell's height. Water can flow from any cell adjacent to an 
ocean into the ocean.

Return a 2D list of grid coordinates 'result' where 'result[i] = [r_i, c_i] denotes 
that rain water can flow from cell (r_i, c_i) to both the Pacific and Atlantic oceans.

Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation:

The following cells can flow to the Pacific and Atlantic oceans, as shown below:

[0,4]:  [0,4] -> Pacific Ocean
        [0,4] -> Atlantic Ocean
[1,3]:  [1,3] -> [0,3] -> Pacific Ocean
        [1,3] -> [1,4] -> Atlantic Ocean
[1,4]:  [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
        [1,4] -> Atlantic Ocean
[2,2]:  [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]:  [3,0] -> Pacific Ocean 
        [3,0] -> [4,0] -> Atlantic Ocean
[3,1]:  [3,1] -> [3,0] -> Pacific Ocean 
        [3,1] -> [4,1] -> Atlantic Ocean
[4,0]:  [4,0] -> Pacific Ocean 
        [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and 
Atlantic oceans.

Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
'''
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # edge case
        if not heights or not heights[0]:
            return []
        
        # get number of rows and columns
        rows, cols = len(heights), len(heights[0])
        
        # set of cells that can flow to each ocean
        atlantic = set()
        pacific = set()
        
        # DFS
        def dfs(r, c, visited, prev_height):
            # base cases: out of bounds, already visited, uphill flow
            if (r < 0 or r >= rows or c < 0 or c >= cols or \
                    (r, c) in visited or heights[r][c] < prev_height):
                return
            
            # mark cell as visited
            visited.add((r, c))
            
            # possible directions of movement (up, down, left, right)
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
                
        # dfs for pacific ocean
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0]) # left edge
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c]) # top edge
            
        # dfs for atlantic ocean
        for r in range(rows):
            dfs(r, cols - 1, atlantic, heights[r][cols - 1]) # right edge
        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows - 1][c]) # bottom edge
            
        # intersection of set is cells that can flow to both
        result = list(pacific & atlantic)
        
        return result