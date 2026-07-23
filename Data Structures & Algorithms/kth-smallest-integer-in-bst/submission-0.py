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

            if node is None or answer is not None:
                return 

            inorder(node.left)

            count+=1 
            if k==count:
                answer = node.val
              
            inorder(node.right)
        
        inorder(root)
        return answer