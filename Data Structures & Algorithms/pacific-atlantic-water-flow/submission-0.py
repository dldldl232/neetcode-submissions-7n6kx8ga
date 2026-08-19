class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        # Sets to store coordinates that can reach each ocean
        pac, atl = set(), set()

        def r_dfs(r, c, visit, prev_height):
            # 1. Check bounds
            # 2. Check if already visited (prevents infinite loops)
            # 3. Check if we can "climb" (current must be >= previous)
            if (
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                (r, c) in visit or 
                heights[r][c] < prev_height
            ):
                return
            
            # Mark this cell as reachable
            visit.add((r, c))
            
            # Explore neighbors
            r_dfs(r + 1, c, visit, heights[r][c])
            r_dfs(r - 1, c, visit, heights[r][c])
            r_dfs(r, c + 1, visit, heights[r][c])
            r_dfs(r, c - 1, visit, heights[r][c])

        # Start DFS from the top and bottom rows
        for c in range(COLS):
            r_dfs(0, c, pac, heights[0][c])             # Top edge (Pacific)
            r_dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # Bottom edge (Atlantic)

        # Start DFS from the left and right columns
        for r in range(ROWS):
            r_dfs(r, 0, pac, heights[r][0])             # Left edge (Pacific)
            r_dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # Right edge (Atlantic)

        # The result is the intersection (&) where a cell exists in both sets
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res