# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if root is None:
        #     return 0
        # queue = deque([root])
        # while queue:
        #     #process node here 
        #     if currNode.left:
        #         queue.append((currNode.left))
        #     if currNode.right:
        #         queue.append((currNode.right))
        

        queue = deque([(p, q)])
        while queue: 
            pNode, qNode = queue.popleft() 
            
            if pNode is None and qNode is None:
                continue 
            if pNode is None or qNode is None: 
                return False 
            if pNode.val != qNode.val:
                return False 
          
            queue.append((pNode.left, qNode.left))
            queue.append((pNode.right, qNode.right))
            
            
        return True