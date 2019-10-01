class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def cycle_check(head):
    seen = []
    current_node = head
    while current_node:
        if current_node in seen:
            return True
        else:
            seen.append(current_node)
        current_node = current_node.next
    return False


a = Node(1)
b = Node(2)
c = Node(3)
d = Node (5)

a.next = b
b.next = c
c.next = d
d.next = a #cycle

print(cycle_check(a))
