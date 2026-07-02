# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # inorder: left -> root -> right

        # from preorder we can know that the first one is the root
        # since we know  the root from inorder we can know that 
        # the left side from the root is in the left branch and right side is on the right branch

        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(
            preorder[1: mid+1],
            inorder[:mid]
        )

        root.right = self.buildTree(
            preorder[mid+1:],
            inorder[mid+1:]
        )

        return root
