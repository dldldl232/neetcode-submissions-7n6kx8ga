class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        rough idea:
        we start from each position we have two chocies: stop or continue

        base case:
        we would need a step param that checks if the step == len(s) - 1. Then we stop and
        check if the path we explored is valid -> but this check we do each step

        How do we check if the path is a palindrome? we check every time we add
        then we have a decision to make cut or not.

        """
        result = []
        path = []
        
        def is_pal(l, r):

            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            
            return True

        def dfs(step):
            if step == len(s):
                result.append(path.copy())
                return
            
            for i in range(step, len(s)):
                if is_pal(step, i):
                    path.append(s[step:i+1])
                    dfs(i+1)
                    path.pop()
        
        dfs(0)
        return result