# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        # Step 2: Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Step 3: Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Step 4: Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next
