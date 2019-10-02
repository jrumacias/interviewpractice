# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_two_lists(l1, l2):
    ret_cur = ListNode(-1)
    head = ret_cur

    while l1 and l2:
        if l1.val < l2.val:
            ret_cur.next = ListNode(l1.val)
            l1 = l1.next
            ret_cur = ret_cur.next
        elif l2.val < l1.val:
            ret_cur.next = ListNode(l2.val)
            l2 = l2.next
            ret_cur = ret_cur.next
        elif l1.val == l2.val:
            ret_cur.next = ListNode(l1.val)
            ret_cur.next.next = ListNode(l2.val)
            ret_cur = ret_cur.next.next
            l1 = l1.next
            l2 = l2.next
    if l1 == None and l2 != None:
        while l2:
            ret_cur.next = ListNode(l2.val)
            l2 = l2.next
            ret_cur = ret_cur.next
    elif l2 == None and l1 != None:
        while l1:
            ret_cur.next = ListNode(l1.val)
            l1 = l1.next
            ret_cur = ret_cur.next
    return head.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(4)

def print_linked_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next

head_node = merge_two_lists(l1, l2)
print_linked_list(head_node)
