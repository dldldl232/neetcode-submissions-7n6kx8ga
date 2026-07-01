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
        
        def dfs(node, max_val_node):
            nonlocal count

            if node is None:
                return 0
            
            if node.val >= max_val_node:
                count += 1
            
            max_val_node = max(node.val, max_val_node)
            
            left_branch = dfs(node.left, max_val_node)
            right_branch = dfs(node.right, max_val_node)

            return count
        

        return dfs(root, root.val)

