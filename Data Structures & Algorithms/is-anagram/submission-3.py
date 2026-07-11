class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # since orders or characters can be different -> would be difficult to use pointers
        # so we would have to track frequency of characters -> would have to use hash sets

        # edge cases:
        if len(s) != len(t):
            return False

        # 1. create hashsets for each strings to track frequency
        s_dict = {}
        t_dict = {}

        # 2. now we would loop through each strings to track frequency
        for i in range(len(s)):
            if s[i] in s_dict: # in Python accessing keys that don't exist immediately raises KeyError
                s_dict[s[i]] += 1
            else: 
                s_dict[s[i]] = 1

        # 3. then we would have to compare the frequency
        # how would we compare?
        # instead of looping through both strings
        # we track the frequency for one string, and for the other string we check if 
        # key-value exists

        for j in range(len(t)):
            if t[j] in t_dict:
                t_dict[t[j]] += 1
            else:
                t_dict[t[j]] = 1

        print(f"s_dict: {s_dict}")
        print(f"t_dict: {t_dict}")
        # now we would have to compare the frequency between dictionaries 
        return t_dict == s_dict
        
