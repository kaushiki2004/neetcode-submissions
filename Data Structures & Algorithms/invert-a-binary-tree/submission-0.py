# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev(node):
            if node.left:
                rev(node.left)
            if node.right:
                rev(node.right)
            node.left,node.right = node.right,node.left
            return node
        if not root:
            return 
        return rev(root)
        