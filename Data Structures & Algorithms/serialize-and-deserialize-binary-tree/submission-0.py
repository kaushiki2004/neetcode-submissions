# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr=[]
        def bfs(root):
            if not root:
                arr.append("N")
                return 
            arr.append(str(root.val))
            bfs(root.left)
            bfs(root.right)
        bfs(root)
        return ",".join(arr)
  
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        i=0
        
        def dfs():
            nonlocal i
            if vals[i] == "N":
                i+=1
                return None
            node = TreeNode(int(vals[i]))
            i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

