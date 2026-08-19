from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            "]": "[",
            ")": "(",
            "}": "{"
            }

        stk = []
        for char in s:
            if char in bracket_dict:
                if stk == []:
                    return False

                if bracket_dict[char] == stk[-1]:
                    stk.pop()
                    continue
            
            stk.append(char)

        if stk == []:
            return True
        else:
            return False