class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        input is n -> then we create n x n list

        we just have to check vertical and diagonals as we are going to loop through every
        row.

        diagonal pattern: 
        down right: (0,0) (1,1), (2,2), (3,3)
        down left:  (0,3) (1,2), (2,1), (3,0)

        so for Q position (i, j)
        it would be
        left: (i-1, j-1)
        right:(i+1, j+1)
        till it hits the end of the column so once we reach n-1 col we stop even though we
        have row num left

        => NONONO
        Down right diag: r - c == 0
        e.g. (0,0), (1,1), (2,2)

        Down left diag: r + c == n - 1
        e.g. (0, 3), (1,2), (2,1), (3,0)
        -> they all produce same result

        so now dfs(i)
        - i would represent which row
        - append path to result at i == n

        it would recurse for each col position 



        """
        res = []
        path = []
        # chessboard = [["."] * n for _ in range(n)] -> do not need
        C = set()
        dL = set() # down left diagonal
        dR = set() # down right diagonal

        def dfs(i):
            if i == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in path])
                return
            
            for col in range(n):
                if col in C or i - col in dL or i + col in dR:
                    continue

                path.append(col)
                C.add(col)
                dL.add(i - col)
                dR.add(i + col)

                dfs(i + 1)

                path.pop()
                C.remove(col)
                dL.remove(i - col)
                dR.remove(i + col)
                    
        dfs(0)
        return res


                 














        
        