# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currNode = root 
        low = min(p.val, q.val)
        high = max(p.val, q.val)
        while currNode:
            #if both q and p are greater go right 
            #if both p and q are smaller go left 
            #return the node else 
            
            if low <= currNode.val <= high: 
                return currNode 
            elif high < currNode.val:
                currNode = currNode.left 
            
            #both p and q are greater 
            else:
                currNode = currNode.right 
         
