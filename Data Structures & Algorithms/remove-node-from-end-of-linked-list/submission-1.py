# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # how do we remove the nth node from the end?
        # maybe we could use two pointers: slow fast
        # when fast is at end then we check the distance of slow and fast and n value

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n+1): # reason why we have range n+1 is cause we want to stop slow at one node before the target
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next