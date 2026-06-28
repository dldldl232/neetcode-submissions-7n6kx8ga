class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False

        # Check if first row has any zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # Use first row and first column as markers
        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Zero rows based on first column markers
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(cols):
                    matrix[r][c] = 0

        # Zero columns based on first row markers
        for c in range(cols):
            if matrix[0][c] == 0:
                for r in range(rows):
                    matrix[r][c] = 0

        # Zero first row if needed
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0