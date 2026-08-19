# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we invert the nodes in the order of top to down so we start from root
        # we would do this by recursion
        if not root.val:
            return root

        root.left, root.right = root.right, root.left
        root = self.invertTree(root)

        