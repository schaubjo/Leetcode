class MinStack:

    def __init__(self):
        self.stack = []
        self.runningMinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.runningMinStack:
            self.runningMinStack.append(min(self.runningMinStack[-1], val))
        else:
            self.runningMinStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.runningMinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.runningMinStack[-1]


test1 = MinStack()
test1.push(1)
test1.push(2)
test1.push(3)
print(test1.top())
print(test1.getMin())
test1.pop()
print(test1.top())
print(test1.getMin())
test1.pop()
print(test1.top())
print(test1.getMin())
