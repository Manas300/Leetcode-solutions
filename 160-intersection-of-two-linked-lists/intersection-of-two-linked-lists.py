# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        lenA, lenB = getLength(headA), getLength(headB)
            # Align the starts of both lists
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
    
        # Traverse together to find the intersection
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
    
        return None

        
        