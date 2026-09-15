from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        if not grid[0]: return 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        numberOfIslands = 0
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r:int, c:int):
             q = collections.deque()
             visit.add((r, c))
             q.append((r, c))

             while q:
                row, col = q.pop()
                for dr, dc in directions:
                    r1 = row + dr
                    c1 = col + dc
                    if r1 in range(rows) and c1 in range(cols):
                        if grid[r1][c1] == "1" and (r1, c1) not in visit:
                            visit.add((r1, c1))
                            q.append((r1, c1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    numberOfIslands += 1
        return numberOfIslands



