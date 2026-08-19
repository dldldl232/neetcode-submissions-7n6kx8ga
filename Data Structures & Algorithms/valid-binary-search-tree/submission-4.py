# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None:
                return True

            if node.left and node.left.val > node.val:
                return False
            
            if node.right and node.right.val < node.val:
                return False
            
            left_branch = dfs(node.left)
            right_branch = dfs(node.right)

            return left_branch and right_branch
        
        return dfs(root)