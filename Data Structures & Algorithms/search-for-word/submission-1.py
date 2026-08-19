class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # prevent repetition

        # explore part
        # i is the index in word we need to match
        def dfs(r, c, i):
            if i == len(word):
                return True

            # out for range, closed, or alphabet does not match
            if (min(r, c) < 0 or r >= ROWS or
            c >= COLS or word[i] != board[r][c] or
            (r, c) in path):
                return False

            # choose curr path
            path.add((r,c))
            # recursion 
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or 
                   dfs(r, c - 1, i + 1))

            # restore path to original state
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    # if dfs returns True
                    return True
        return False
                
            
            