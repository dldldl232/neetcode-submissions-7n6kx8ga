class Solution:
    def firstUniqChar(self, s: str) -> int:
        # two pointer
        # one stays and if repeating move
        # other one moves and keeps being compared
        # but we would have to use inner loops -> inefficient
        repeated_char = set()
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    repeated_char.add(s[j])
                    break # moves the i ptr
                    
            # I did not refresh the state of repeated
            # if not repeated:
            #     print(f"i: {i}")
            #     return i

            if s[i] not in repeated_char:
                return i
    
        return -1
            
            


        