class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        popped = self.stack[-1]
        if popped == self.minVal:
            newMin = float('inf')
            for i in range(len(self.stack) - 1):
                newMin = min(newMin, self.stack[i])
            self.minVal = newMin
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal


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
