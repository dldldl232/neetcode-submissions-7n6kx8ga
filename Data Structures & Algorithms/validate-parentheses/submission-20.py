class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stk = deque()

        if len(s) == 1:
            return False
        
        if not len(s):
            return True

        for char in s:
            if char in ['(', '{', '[']:
                stk.append(char)
            elif char in d:
                if len(stk) == 0:
                    return False
                elif stk[-1] == d[char]:
                    stk.pop()
                else:
                    stk.append(char)
        
        return len(stk) == 0


        