class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # output is boolean
        # we start from each position and move left right top down
        # dir = [(-1,0), (1,0), (0, 1), (0, -1)]
        # we recurse all of those paths and backtrack/stop when
        # 1) we cannot move further (e.g. end of col, end of row)
        # 2) the len(path) == len(word):
        #    then we check if the path we found (this is inefficient)

        # we can rather check if the first position match the word[0] if so then we 
        # start the recursion then continue this pattern 
        # for each direction we move to we check if the char match with word[i+1]

        """The same cell may not be used more than once"""
        """For cases like seen"""
        ROWS, COLS = len(board), len(board[0])
        path = set() # we have to prevent repition we use set

        # i is for length count
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))

            res = (
                dfs(r + 1, c, i + 1) or 
                dfs(r - 1, c, i + 1) or 
                dfs(r, c - 1, i + 1) or
                dfs(r, c + 1, i + 1))

            path.remove((r,c))
            return res
        

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        
        return False