"""Optimization"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        required = len(need)
        window_count = {}
        matches = 0
        m = len(s1)

        for r in range(len(s2)):
            # before check
            if window_count.get(s2[r], 0) == need[s2[r]]:
                matches -= 1
            
            # after check
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1
            if window_count[s2[r]] == need[s2[r]]:
                matches += 1
            
            if r >= m:
                if window_count[s2[r-m]] == need[s2[r-m]]:
                    matches -= 1

                window_count[s2[r-m]] -= 1
                if window_count[s2[r-m]] == need[s2[r-m]]:
                    matches += 1
            
            if matches == required:
                return True
        
        return False

        