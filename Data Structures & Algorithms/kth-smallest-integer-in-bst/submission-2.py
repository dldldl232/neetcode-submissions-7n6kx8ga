# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None

        def search(node):
            nonlocal count, answer

            if node is None or answer is not None:
                return

            # 1. Visit left subtree
            search(node.left)

            # 2. Visit current node
            count += 1
            if count == k:
                answer = node.val
                return

            # 3. Visit right subtree
            search(node.right)

        search(root)
        return answer