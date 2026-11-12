class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we store the coordination of the cell
        # return cell that can reach both Pacific and Atlantics
        res = []
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(heights), len(heights[0])
        atlantic, pacific = set(), set()

        def search(start, reached):
            q = deque([start])
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc 

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if heights[r][c] <= heights[nr][nc] and (nr, nc) not in reached:
                            q.append((nr,nc))
                            reached.add((nr, nc))

        # pacific search
        # we only start from (0, col), (row, 0)
        for r in range(rows):
            pacific.add((r,0))
            search((r,0), pacific)
        
        for c in range(cols):
            pacific.add((0,c))
            search((0,c), pacific)

        # atlantic search
        # we only start from (2, col), (row, cols)
        for r in range(rows):
            atlantic.add((r, cols-1))
            search((r, cols-1), atlantic)
        
        for c in range(cols):
            atlantic.add((rows-1, c))
            search((rows-1, c), atlantic)

        
        # now find union
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res
