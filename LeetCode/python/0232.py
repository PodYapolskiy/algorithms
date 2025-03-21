class MyQueue:
    def __init__(self):
        self.write = []
        self.read = []
        self.front = None

    def push(self, x: int) -> None:
        if len(self.write) == 0:
            self.front = x  # helps when peek
        self.write.append(x)

    def pop(self) -> int:
        if len(self.read) == 0:
            while len(self.write) > 0:  # reverse from write to read stack
                self.read.append(self.write.pop())
        return self.read.pop()

    def peek(self) -> int:
        if len(self.read) > 0:
            return self.read[-1]
        return self.front

    def empty(self) -> bool:
        return len(self.write) == 0 and len(self.read) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
