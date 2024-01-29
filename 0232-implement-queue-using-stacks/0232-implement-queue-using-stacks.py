class MyQueue:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        return
    
    def pop(self) -> int:
        if not self.empty():
            return self.stack.popleft()
        
    def peek(self) -> int:
        if not self.empty():
            return self.stack[0]
        
    def empty(self) -> bool:
        if self.stack:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()