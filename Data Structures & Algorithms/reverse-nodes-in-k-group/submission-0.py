# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check step length
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        
        if count < k:
            return head # fewer than k then leave as it is
        
        prev = None
        curr = head
        for _ in range(k):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        # recursively handle the rest and attach
        head.next = self.reverseKGroup(curr, k)

        return prev