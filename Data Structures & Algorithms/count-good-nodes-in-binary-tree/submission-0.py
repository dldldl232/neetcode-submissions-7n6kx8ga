# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # will use dfs approach
        root_val = root.val
        count = 0
        
        def dfs(node, prev):
            nonlocal count
            
            if node is None:
                return 0
            
            if node.val >= prev.val and node.val >= root_val:
                count += 1
            
            left_branch = dfs(node.left, node)
            right_branch = dfs(node.right, node)

            return count
        

        return dfs(root, root)

