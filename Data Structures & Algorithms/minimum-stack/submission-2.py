class MinStack:

    def __init__(self):
        self.stk = []      
        self.currMin = []

    def push(self, val: int) -> None:
        if len(self.currMin) == 0:
            self.currMin.append(val)
        else:
            pushElem = min(self.currMin[-1], val)
            self.currMin.append(pushElem)

        self.stk.append(val)
        
    def pop(self) -> None:
        if len(self.stk) == 0:
            raise IndexError("Cannot pop empty stack")

        self.stk.pop()
        self.currMin.pop()
        # if popped == self.currMin[-1]:
        #     self.currMin.pop()
                
    def top(self) -> int:
        if len(self.stk) == 0:
            raise IndexError("Stack is empty")
        
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.currMin[-1]
        
