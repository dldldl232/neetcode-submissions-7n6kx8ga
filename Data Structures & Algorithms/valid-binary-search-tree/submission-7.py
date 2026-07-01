# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we did not consider that all left must be smaller than root and 
        # all right must be bigger than root

        def dfs(node, low, high):
            if node is None:
                return True
            
            if low >= node.val or node.val >= high:
                return False
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
            
        
        return dfs(root, float("-inf"), float("inf"))