class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        DP = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if not DP[i][j]:
                    if s[i] == s[j] and (j - i <= 2 or DP[i+1][j-1]):
                        DP[i][j] = True
                        count += 1
        
        return count
