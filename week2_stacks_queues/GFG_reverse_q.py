# Reversing a Queue
# Give an algorithm for reversing a queue Q. Only following standard operations
# are allowed on queue.

# enqueue(x) : Add an item x to rear of queue.
# dequeue() : Remove an item from front of queue.
# empty() : Checks if a queue is empty or not.

# Input : Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Output :Q = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# Input :[1, 2, 3, 4, 5]
# Output :[5, 4, 3, 2, 1]

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def reverse_q(self):
        if self.is_empty():
            return self
        rev_q = []
        for i in range(0, self.size()):
            rev_q.append(self.dequeue())
        return rev_q

q = Queue()
q.enqueue(1)
print("1 added to Q")
q.enqueue(2)
print("2 added to Q")
q.enqueue(3)
print("3 added to Q")
q.enqueue(4)
print("4 added to Q")
q.enqueue(5)
print("5 added to Q")
print(q.reverse_q())
