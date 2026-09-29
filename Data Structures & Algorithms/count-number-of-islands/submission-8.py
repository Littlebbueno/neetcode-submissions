from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visits = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if grid[r][c] != "1" or (r, c) in visits:
                return
            visits.add((r, c))
            for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)):
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visits:
                    dfs(r, c)
                    res += 1
        return res 
