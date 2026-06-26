class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1] * n 

        def dfs(i):
            if i == n:
                return 1
            
            if memo[i] != -1:
                return memo[i]
            
            if s[i] == "0":
                return 0
            
            ways = dfs(i+1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
            
            memo[i] = ways
            return memo[i]
        
        return dfs(0)
    

    # since it is a counting problem with multiple valide choices
    # we usually add them