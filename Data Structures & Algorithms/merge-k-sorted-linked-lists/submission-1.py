# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Algorithm:
1. push the head node of every non-empty list into a min-heap (size <= k)
2. pop the smallest node from the heap - that's the next node in your merged result
3. if that node has a .next, push .next into the heap
4. repeat until the heap is empty
"""
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # we have to merge sorted linked list
        heap = []

        # step 1
        # we use counter as tiebreaker as ListNode isn't comparable
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            
        
        return dummy.next
