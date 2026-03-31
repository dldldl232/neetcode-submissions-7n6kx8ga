# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # problem is that we do not know the total length of the LL
        # we can create a ptr that points to the end of the LL
        temp = head
        curr = head
        count = 1

        while temp:
            if temp.next == None:
                break

            temp = temp.next
            count+=1
        
        mid = count // 2
        print(mid)

        for i in range(mid):
            curr = curr.next
        
        return curr
            
