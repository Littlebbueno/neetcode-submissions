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
        def dfs(row, col):
            queue = deque()
            queue.append((row, col))
            while queue:
                r1, c1 = queue.popleft()
                for value in directions:
                    dr, dc = value
                    if (r1 + dr) in range(rows) and (c1 + dc) in range(cols):
                        if (r1+dr,c1+dc) not in visits and grid[r1+dr][c1+dc] == "1":
                            visits.add((r1+dr,c1+dc))
                            queue.append((r1+dr,c1+dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visits:
                    visits.add((r,c))
                    dfs(r, c)
                    res += 1
        return res 
