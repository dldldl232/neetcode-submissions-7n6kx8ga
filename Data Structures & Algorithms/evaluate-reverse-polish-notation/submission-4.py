class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {'+', '-', '/', '*'}

        for c in tokens:
            if c not in ops:
                stk.append(int(c))
            else:
                right = stk.pop()
                left = stk.pop()

                if c == '+':
                    stk.append(left+right)
                elif c == '-':
                    stk.append(left-right)
                elif c == '/':
                    stk.append(int(left/right))
                elif c == '*':
                    stk.append(left*right)
        
        return stk[0]