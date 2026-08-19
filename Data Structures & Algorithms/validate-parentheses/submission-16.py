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
            if char == '(' or char == '{' or char == '[':
                stk.append(char)
            elif char in d:
                if stk[-1] == d[char]:
                    stk.pop()
        
        return len(stk) == 0


        