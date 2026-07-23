# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None 
        root = TreeNode(preorder[0])
        st = [root] 
        i = 0 

        for value in preorder[1:]:
            node = TreeNode(value) 
            if st[-1].val != inorder[i]:
                st[-1].left = node 
            else:
                parent = None 
                while st and i < len(inorder) and st[-1].val == inorder[i]:
                    parent = st.pop()
                    i+=1 
                parent.right = node 
            st.append(node)
        return root 