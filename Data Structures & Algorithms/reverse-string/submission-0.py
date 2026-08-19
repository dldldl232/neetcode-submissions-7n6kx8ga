class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s == []:
            return []
        
        s_dict = {}

        for i, a in enumerate(s):
            s_dict[i] = a
        
        # i + j == len(s)
        length = len(s) - 1
        for j in range(len(s)):
            s[j] = s_dict[length-j]
            