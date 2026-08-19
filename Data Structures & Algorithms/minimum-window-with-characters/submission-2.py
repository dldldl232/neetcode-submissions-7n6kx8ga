import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = Counter(t)
        required = len(need)
        window_count = {}
        matches = 0
        m = len(t)
        min_length = float('inf')
        l = 0

        for r in range(len(s)):
            print(f"{r} : {s[r]}")
            if s[r] not in need:
                continue
            
            # if char exist in need
            if window_count.get(s[r], 0) == need[s[r]]:
                matches -= 1
            
            window_count[s[r]] = window_count.get(s[r], 0) + 1
            if window_count[s[r]] == need[s[r]]:
                matches += 1
            
            while matches == required:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    start = l

                if s[l] not in need:
                    l+=1
                    continue

                if window_count[s[l]] == need[s[l]]:
                    matches -= 1

                window_count[s[l]] -= 1
                if window_count[s[l]] == need[s[l]]:
                    matches += 1
                
                l += 1
        
        
        return s[start:start + min_length] if min_length != float('inf') else ""