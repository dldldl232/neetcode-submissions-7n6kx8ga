from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,-1), (0, 1)] 

        q = deque()      

        # Step 1: scan the grid, put every treasure (0) in the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))


        # Step 2: while the queue isn't empty:
        #     pop a cell
        #     for each of 4 directions:
        #         compute the neighbor
        #         if it's in bounds AND still INF:
        #             set its distance (based on the cell you popped)
        #             add it to the queue

        while q:
            r, c = q.popleft() # we want to get the front
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == INF:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))

            