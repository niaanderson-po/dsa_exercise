# Class to count the number of islands in a grid using BFS, where '1' represents land and '0' represents water.
from collections import deque

class Solution:
    
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            queue = deque()
            visit.add((r,c))
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                direction = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direction:
                    r,c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and 
                        (r,c) not in visit):
                        queue.append([r,c])
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands