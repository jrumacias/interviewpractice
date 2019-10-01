# Implement a singly linked list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print(a.val)
print(a.next.val)
print(a.next.next.val)

current_node = a
while current_node:
    print("Current node's value is: {}".format(current_node.val))
    current_node = current_node.next
