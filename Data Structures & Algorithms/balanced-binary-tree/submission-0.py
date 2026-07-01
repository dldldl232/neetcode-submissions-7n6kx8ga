# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # how to calculate height difference?
        # we would use dfs
        # we dfs through each left and right branch
        # then we would calculate abs(left-right) <= 1
        balanced = True

        def dfs(node):
            nonlocal balanced

            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            height_diff = abs(left_depth - right_depth)

            if height_diff > 1:
                balanced = False

            return 1 + max(left_depth, right_depth)
        
        dfs(root)
        return balanced

        