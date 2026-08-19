class Solution:
    def firstUniqChar(self, s: str) -> int:
        # two pointer
        # one stays and if repeating move
        # other one moves and keeps being compared
        # but we would have to use inner loops -> inefficient
        repeated_char = set()
        
        for i in range(len(s)):
            repeated = False
            print(f"ptr1: {s[i]}")
            print(f"i+1 value: {i+1}")
            for j in range(i+1, len(s)):
                print(f"j value: {j}")
                print(f"ptr2: {s[j]}")
                if s[i] == s[j]:
                    repeated_char.add(s[j])
                    # repeated = True
                    break # moves the i ptr
            print (f"Repeatd:{repeated}") 
            # I did not refresh the state of repeated
            # if not repeated:
            #     print(f"i: {i}")
            #     return i

            if s[i] not in repeated_char:
                return i
    
        return -1
            
            


        