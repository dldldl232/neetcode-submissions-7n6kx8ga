# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""

        curr1 = l1
        curr2 = l2

        while curr1:
            str1 += str(curr1.val)
            curr1 = curr1.next

        while curr2:
            str2 += str(curr2.val)
            curr2 = curr2.next
        
        reversed1 = str1[::-1]
        reversed2 = str2[::-1]

        output = int(reversed1) + int(reversed2)
        output_str = str(output)

        reversed_output = output_str[::-1]
        result = ListNode()
        tail = result

        for i in range(len(reversed_output)):
            tail.next = ListNode(int(reversed_output[i]))
            tail = tail.next
        
        return result.next
