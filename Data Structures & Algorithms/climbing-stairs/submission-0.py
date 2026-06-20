class Solution:
    def climbStairs(self, n: int) -> int:
        # choice is 1. one step or 2. two step
        # we can use recursion to check all the possibilities
        cache = [-1] * n

        # think of i as steps
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]

        return dfs(0)        
