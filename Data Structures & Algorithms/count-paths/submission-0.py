class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return num of possible unique paths
        # from grid[0][0] to grid[m-1][n-1]

        # dp[m][n] = num of possible unique paths
        # dp cause we will divide this into subproblems and use recursion
        # to go through possible paths
        # But we will use memo to improve efficiency

        # choices:
        # 1. go down
        # 2. go right

        # memo[i][j] = store if we visited this cell

        # condtions check would be
        # 1. base case: if we reach grid[m-1][n-1] we increase the count
        # 2. if cell is visited
        # 3. if the cell we visited does not fulfill those conditions
        #    we update the memo[i][j] as visited

        # code will stop once both i and j cannot move anymore
        memo = [[False] * n for _ in range(m)]
        count = 0

        # i = row
        # j = column
        # we would also have to check if i and j are within bounds
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            
            # invalid path
            if i >= m or j >= n:
                return 0
            
            if memo[i][j]:
                return memo[i][j]

            down = dfs(i+1, j)
            right = dfs(i, j+1)
            memo[i][j] = down + right

            return memo[i][j]
            
        return dfs(0, 0)

            