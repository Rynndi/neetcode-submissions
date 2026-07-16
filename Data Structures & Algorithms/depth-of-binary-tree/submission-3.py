# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        #each node has its own height as well 
        st = deque([(root, 1)])
        maxHeight = 0
        while st:
            #unpack tuple 
            currNode, currHeight = st[-1] 
            st.pop()
            maxHeight = max(currHeight, maxHeight)
            if currNode.left:
                st.append((currNode.left, currHeight + 1))
            if currNode.right:
                st.append((currNode.right, currHeight + 1))
        return maxHeight