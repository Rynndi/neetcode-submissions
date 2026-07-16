# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #return level order traversal.
        if root is None: 
            return []  
        st = [] 
        #newList created everytime a new layer is hit 
        queue = deque([(root)]) 

        #inorder: left, root, right 
        while queue: 

            currLevel = [] 
            levelSize = len(queue)
            
            for _ in range(levelSize): 
                currNode = queue.popleft() 

                if currNode.left: 
                    queue.append(currNode.left)
                #process node here. 
                currLevel.append(currNode.val)
                
                if currNode.right: 
                    queue.append(currNode.right)
            st.append(currLevel)
        return st 

        #st at this point is [1, 2, 3]

       
