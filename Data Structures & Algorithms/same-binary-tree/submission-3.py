# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(tree1, tree2):
            if tree1 is None or tree2 is None:
                return 0

            if tree1.val != tree2.val:
                return False
            
            left_branch = dfs(tree1.left, tree2.left)
            right_branch = dfs(tree1.right, tree2.right)

            return True
        
        return dfs(p, q)