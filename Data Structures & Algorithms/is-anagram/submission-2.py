class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # contain only the exact same characters
        # order wouldn't matter since it can be different
        # only the count of the alphabet would matter
        # so I would use hashmaps
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for char in s:
            s_dict[char] += 1

        for char in t:
            t_dict[char] += 1
        
        return s_dict == t_dict
