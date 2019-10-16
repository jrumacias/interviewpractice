# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList(head):
    if not head or not head.next:
        return head

    oddptr = head
    evptr = head.next
    evhead = evptr

    while evptr and evptr.next:
        oddptr.next = evptr.next
        oddptr = oddptr.next
        evptr.next = oddptr.next
        evptr = evptr.next

    oddptr.next = evhead
    return head