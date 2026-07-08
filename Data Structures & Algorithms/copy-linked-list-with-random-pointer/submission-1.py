"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        original_to_copy = {}

        curr = head

        # create a hash map where we store the copy and key so we can retrieve
        # information regarding the copy
        # since for deepcopy the copy shouldn't point to original node attributes like
        # next or random
        while curr:
            original_to_copy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            copied = original_to_copy[curr]

            copied.next = original_to_copy.get(curr.next) # we use get to handle None
            copied.random = original_to_copy.get(curr.random)

            curr = curr.next
        
        return original_to_copy[head]        
