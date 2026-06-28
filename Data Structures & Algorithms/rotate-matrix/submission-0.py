class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # step 1
        # transpose -> we swap matrix[row][col] with matrix[col][row]

        # step 2
        # we reverse each row

        # -> we get final rotated matrix
        n = len(matrix)
        
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        # why range(row+1, n)?
        # for transpose, we only want to swap the upper triangle with the lower triangle
        # we do not touch diagnol
            
        for row in range(n):
            matrix[row].reverse()