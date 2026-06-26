class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)

        def dfs(rem):
            if rem == 0:
                return 0
            
            if rem < 0:
                return float("inf")
            
            if memo[rem] != -1:
                return memo[rem]
            
            best = float("inf")

            for coin in coins:
                best = min(best, 1+dfs(rem-coin))
            
            memo[rem] = best
            return memo[rem]
        
        ans = dfs(amount)

        if ans == float("inf"):
            return -1
        return ans