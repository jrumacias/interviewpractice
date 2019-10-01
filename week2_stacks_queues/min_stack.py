class MinStack:

    def __init__(self):
        self.items = []
        self.min_stack = []

    def pop(self):
        if self.items[-1] == self.min_stack[-1]:
            self.items.pop()
            self.min_stack.pop()
        else:
            self.items.pop()

    def peek(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)
        if self.min_stack and item <= self.min_stack[-1]:
            self.min_stack.append(item)
        elif not self.min_stack:
            self.min_stack.append(item)
    def min(self):
        return self.min_stack[-1]

ms = MinStack()
# ms.push(5)
# ms.push(10)
# print(ms.min())
# ms.pop()
# ms.push(4)
# print(ms.min())
# ms.pop()
# print(ms.min())

ms.push(0)
ms.push(1)
ms.push(0)
print(ms.min())
ms.pop()
print(ms.min())
