def uniqueShapesInMatrix(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    unique_shapes = set()
    
    # 8 possible directions: up, down, left, right, and 4 diagonals
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),  # cardinal directions
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # diagonals
    ]
    
    def dfs(r, c, base_r, base_c, shape):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            grid[r][c] == 0 or (r, c) in visited):
            return
        visited.add((r, c))
        shape.append((r - base_r, c - base_c))  # relative coordinates
        for dr, dc in directions:
            dfs(r + dr, c + dc, base_r, base_c, shape)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                shape = []
                dfs(r, c, r, c, shape)
                unique_shapes.add(tuple(shape))
    
    return len(unique_shapes)

# Example usage
grid = [
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1]
]

print(uniqueShapesInMatrix(grid)) 