class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        DP = [[False] * n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or DP[i+1][j-1]):
                    DP[i][j] = True

                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
        
        return s[resIdx : resIdx + resLen]

