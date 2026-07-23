# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        st = deque([(root, float("-inf"), float("inf"))])
        while st: 
            currNode, lowerBound, upperBound = st.popleft()
            if not (lowerBound < currNode.val < upperBound):
                return False 
            #go left -> tighten upper bound 
            if currNode.left:
                st.append((currNode.left, lowerBound, currNode.val))
            #go right -> tighten lower bound 
            if currNode.right:
                st.append((currNode.right, currNode.val, upperBound))
                    
        return True 
        