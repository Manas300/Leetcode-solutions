# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Previous node, initially None
        current = head  # Current node, initially the head of the list
    
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move the previous pointer forward
            current = next_node  # Move to the next node
    
        return prev 
        