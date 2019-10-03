# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_duplicates(head):
    if not head or not head.next:
        return head
    seen = set()
    curnode = head
    prevnode = None
    nextnode = None

    while curnode:
        # if we've already seen this value
        if curnode.val in seen:
            prevnode.next = curnode.next
            nextnode = curnode.next
            curnode.next = None
        else:
            seen.add(curnode.val)
            prevnode = curnode
            nextnode = curnode.next
        curnode = nextnode
    return head
