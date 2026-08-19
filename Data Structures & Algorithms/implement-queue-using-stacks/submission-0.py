class MyQueue:

    def __init__(self):
        self.storage = []
        

    def push(self, x: int) -> None:
        self.storage.append(x)
        

    def pop(self) -> int:
        pop_value = self.storage[0]
        self.storage.remove(pop_value)
        return pop_value

    def peek(self) -> int:
        return self.storage[0]
        

    def empty(self) -> bool:
        if self.storage is None:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()