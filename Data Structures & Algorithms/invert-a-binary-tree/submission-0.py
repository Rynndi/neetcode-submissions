# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #BFS algo on a tree: 
        if root is None:
            return 
        queue = deque([root])
        while queue:
            currNode = queue.popleft() 
            
            #process(currentNode)
            currNode.left, currNode.right = currNode.right, currNode.left
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        return root
        