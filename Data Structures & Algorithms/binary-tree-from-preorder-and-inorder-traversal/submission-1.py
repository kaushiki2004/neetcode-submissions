# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index = {val: i for i, val in enumerate(inorder)}
        pre_i=0

        def build(left,right):
            nonlocal pre_i
            if left>right:
                return None
            curr = TreeNode(preorder[pre_i])
            pre_i+=1
            mid = index[curr.val]

            curr.left = build(left,mid-1)
            curr.right =  build(mid+1,right)

            return curr
        return build(0,len(inorder)-1)

