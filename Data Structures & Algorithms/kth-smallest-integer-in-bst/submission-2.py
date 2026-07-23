# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #easiest approached as a recursive problem. 
        count = 0 
        answer = None 
      
        def inorder(node):
            nonlocal count, answer 
            if node is None:
                return 

            inorder(node.left)
            count+=1
            if k==count:
                #this returns from the current recursive call, but not from every older call. The result has to be propagated through an answer. 
                answer = node.val
                return

            inorder(node.right)
        
        inorder(root)
        return answer
      