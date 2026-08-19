from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # return true if s2 contains a permutation of s1
        # doesn't have to be exact ordering, but they do have to be continuous

        """
        Possible approach:
        We first store the length of s1 len_s1 = len(s1) = 3

        Then for each starting position is s2 we check if the following substring (that follows
        the length of s1) is a permutation of s1.

        Now how do we check if it is a permuation?
        We will use Counter(s1) == Counter(s2)
        """

        len_s1 = len(s1)

        for i in range(len(s2)):
            if i + len_s1 > len(s2):
                return False
            
            if sorted(s2[i:i+len_s1]) == sorted(s1):
                return True
        
        

