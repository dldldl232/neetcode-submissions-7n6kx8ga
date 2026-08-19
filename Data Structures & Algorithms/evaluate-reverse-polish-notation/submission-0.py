class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Assume that division between integers always truncates toward zero.
        # -> means we have to use int(a/b)
        stk = []
        
        for c in tokens:
            if c == '+':
                elem2 = stk.pop()
                elem1 = stk.pop()

                output = elem1 + elem2
                stk.append(output)
            
            elif c == '-':
                elem2 = stk.pop()
                elem1 = stk.pop()
                
                output = elem1 - elem2
                stk.append(output)

            elif c == '*':
                elem2 = stk.pop()
                elem1 = stk.pop()

                output = elem1 * elem2
                stk.append(output)
            
            elif c == "/":
                elem2 = stk.pop()
                elem1 = stk.pop()

                output = int(elem1 / elem2)
                stk.append(output)
            
            else:
                stk.append(int(c))
        
        return output