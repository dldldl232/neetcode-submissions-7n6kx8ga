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
        if head is None:
            return None

        old_to_copy = {}

        # First pass: create a copy of every node
        curr = head

        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: connect next and random pointers
        curr = head

        while curr:
            copied = old_to_copy[curr]

            copied.next = old_to_copy.get(curr.next)
            copied.random = old_to_copy.get(curr.random)

            curr = curr.next

        return old_to_copy[head]