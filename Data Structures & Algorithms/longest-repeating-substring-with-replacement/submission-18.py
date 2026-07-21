class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return the length of the longest substring after k replacement
        
        """
        we can use two pointers. 
        l, r = 0, 1

        if l == r: 
            r += 1
            length += 1
            max_length = max(max_length, length)
        if l != r:
            if k != 0:
                replace r's char with l's char 
                then move r += 1 
                k -= 1
                length += 1
                max_length = max(max_length, length)
        

        repeat until r >= len(s)

        -> this works for existing examples, but we have to check edge cases or diff cases
        EX1
        "XYYXY", k = 2
        My current code doesn't work for this example. The problem is that our current code
        doesn't know or to decide how replacing with what with what is the most effective.
        
        """
        count = {}
        max_freq = 0
        l = 0
        result = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            window_length = r - l + 1
            if window_length - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)

        return result


