from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)

        for i in range(len(s2)):
            if i + len_s1 > len(s2):
                return False
            
            if Counter(s2[i:i+len_s1]) == Counter(s1):
                return True
        
        return False
