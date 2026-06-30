# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True

            if tree1 is None or tree2 is None:
                return False

            if tree1.val != tree2.val:
                return False
            
            left_branch = dfs(tree1.left, tree2.left)
            right_branch = dfs(tree1.right, tree2.right)

            return left_branch and right_branch
        
        return dfs(p, q)