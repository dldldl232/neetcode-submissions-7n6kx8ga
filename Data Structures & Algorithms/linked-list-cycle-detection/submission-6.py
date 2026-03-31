# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # don't think the node value is unique
        # therefore we can't use sets
        # we will use hash maps
        # key will be node value and value will be idx

        # node_dict = {}
        # but since if there is a cycle we do not know when the LL ends
        # assume that node value is unique (not assumption question only works
        # if node value is unique)

        node_value = set()
        node_val_count = {}
        temp = head
        curr = head

        while temp and temp.val not in node_value:
            node_value.add(temp.val)
            temp = temp.next
        
        node_list = list(node_value)
        
        for i in range(len(node_value)):
            node_val_count[node_list[i]] = 0

        while curr:
            if node_val_count[curr.val] > 1:
                return True
            node_val_count[curr.val] += 1
            curr = curr.next
        
        return False
        



        