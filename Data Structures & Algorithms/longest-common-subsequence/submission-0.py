class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return the length of the longest common subseq between two strings
        # if one exists, otherwise return 0
        
        # dp = return length of longest common subseq between two strings
        # if exist else return 0

        # so the vague idea of our solution would be:
        # so dfs would match each char between two strings.
        # if identical we increase length
        # if it doesn't match then we have two options
        # 1. stop the search and start from another index
        # 2. eliminate the element and move on

        # in order to do this we would first have to compare lengths
        # longer one would be the one that should have elimination
        # then to implement option 2
        
        # choice
        # 1. choose
        # 2. skip

        # memo[i][j] = store the length of each substring for each position

        n = len(text1) # row
        m = len(text2) # col

        memo = [[-1] * m for _ in range(n)] 

        # i = text1 
        # j = text2
        def dfs(i, j):
            if i >= n or j >= m:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]

            take = 0
            if text1[i] == text2[j]:
                memo[i][j] = 1 + dfs(i+1, j+1)
            else:
                memo[i][j] = max(
                    dfs(i+1, j),
                    dfs(i, j+1)
                )
            
            return memo[i][j]

        return dfs(0,0)