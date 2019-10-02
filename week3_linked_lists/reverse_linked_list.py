# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    current_node = head
    next_node = None
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node

a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)

a.next = b
b.next = c
c.next = d

print(reverseList(a).val)
