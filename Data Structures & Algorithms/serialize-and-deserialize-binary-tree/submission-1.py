# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""

        def dfs(node):
            nonlocal res 
            if node is None:
                res += "0#"
                return 
            val = str(node.val)
            res += str(len(val)) + "#" + val 

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res 

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        def dfs():
            nonlocal i
            j = i
            while data[j] != "#":
                j += 1 
            length = int(data[i:j])
            i = j + 1 
            if length == 0:
                return None 
            val = int(data[i:i + length])
            i += length
            node = TreeNode(val) 
            node.left = dfs() 
            node.right = dfs() 

            return node 

        return dfs()