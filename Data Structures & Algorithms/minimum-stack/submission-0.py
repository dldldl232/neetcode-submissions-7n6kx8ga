class MinStack:

    def __init__(self):
        self.stk = []      
        self.currMin = float("inf")

    def push(self, val: int) -> None:
        self.currMin = min(val, self.currMin)
        self.stk.append(val)
        
    def pop(self) -> None:
        if len(self.stk) == 0:
            raise IndexError("Cannot pop empty stack")

        popped = self.stk.pop()
        if popped == self.currMin:
            self.currMin = float("inf")
            for elem in self.stk:
                self.currMin = min(self.currMin, elem)
                
    def top(self) -> int:
        if len(self.stk) == 0:
            raise IndexError("Stack is empty")
        
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.currMin
        
