# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # we could use recursion and update sum iff value is bigger
        # path = pair of adjacent ndoes has an edge connecting them
        # a node cannot appear in the sequence more than once 
        maxSum = float("-inf")

        def dfs(node):
            nonlocal maxSum

            if not node:
                return 0
            
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            current_path = node.val + left_gain + right_gain

            maxSum = max(maxSum, current_path)

            return node.val + max(left_gain, right_gain)

        
        dfs(root)
        return maxSum