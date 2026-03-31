class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dir = [[1,0], [-1,0], [0,1], [0,-1]]
        island = 0

        def dfs(r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in dir:
                dfs(r+dr, c+dc)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island += 1
        
        return island
