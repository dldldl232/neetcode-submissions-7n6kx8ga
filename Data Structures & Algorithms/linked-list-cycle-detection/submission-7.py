# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # cycle exists if at least one node in the list can be visited again by the next ptr
        # important logic would be keeping track of visited node 
        # node.next = None -> no cycle
        # we will assume that the values of each node are not unique
        # then the remaining way to check if cycle exist is that if node.next visit the same object
        # we would do this by creating a hash table where we store the index : node.val and if we 
        # visit that index again we have a cycle

        temp = head
        visitedNodes = set()

        while temp:
            if temp in visitedNodes:
                return True
            
            visitedNodes.add(temp)
            temp = temp.next
        
        return False

