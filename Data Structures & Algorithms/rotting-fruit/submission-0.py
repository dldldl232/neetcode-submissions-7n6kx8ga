from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # same as treasure islands
        # we start from the rotten fruit (find by scanning)
        # then for each direction/neighbor we check if grid[nr][nc] == 1
        # then we +1 minute

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        res = 0
        fresh = 0

        q = deque()

        # scan for rotten fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        # we start from the q
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            q.append((nr, nc))
                
            res += 1
                
        return res if fresh == 0 else -1
                



