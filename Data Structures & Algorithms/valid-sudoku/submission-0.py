class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        ROW = len(board)
        COL = len(board[0])

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == '.':
                    continue
                elif (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in boxes[(i//3)*3 + (j//3)]):
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3)*3 + (j//3)].add(board[i][j])

        return True