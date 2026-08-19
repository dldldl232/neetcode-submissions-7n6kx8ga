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
                print(f"pop: {char}")
                if len(stk) == 0:
                    stk.append(char)
                elif stk[-1] == d[char]:
                    print(f"top: {stk[-1]}")
                    print(f"d[char]: {d[char]}")
                    stk.pop()
        
        return len(stk) == 0


        