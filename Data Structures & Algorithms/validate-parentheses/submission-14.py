class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stk = deque()

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stk.append(char)
            elif char in d:
                if stk[-1] == d[char]:
                    stk.pop()
        
        return len(stk) == 0


        