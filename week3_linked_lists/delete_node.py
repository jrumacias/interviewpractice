## TODO: Write a function to delete a node (except the tail) in a singly
##       linked list, given only access to that node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should
# become 4 -> 1 -> 9 after calling your function.

def delete_node(target_node):
    
