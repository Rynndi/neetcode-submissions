# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pList = [] 
        qList = [] 

        if root is None: 
            return None 
        
        #each node stores its list + appends itself to it 
        queue = deque([(root, [root])])
        seen = set() 
    
        while queue and len(seen) != 2:
            #unpack tuple 
            currNode, currList = queue.popleft() 
        
            #process node here: 
            if currNode.val == p.val:
                pList = currList 
                seen.add(currNode)
            
            if currNode.val == q.val: 
                qList = currList 
                seen.add(currNode)
            
            #insert node to the front of currNode 
                #make a new path equal to the old path + the child 
                #newList = currList + [currNode.left]
            if currNode.left:
                newList = currList + [currNode.left]
                queue.append((currNode.left, newList))
            if currNode.right: 
                newList = currList + [currNode.right]
                queue.append((currNode.right, newList))
        
        #right now, qList and pList should contain themselves + their parents' nodes. iterate through the shorter list
        #until found the first identical one 
        #walk while they match, remember last shared node 
        lastCommon = None 
        shorterLen = len(qList) if len(qList)<len(pList) else len(pList)
        for i in range(shorterLen):
            if pList[i] == qList[i]:
                lastCommon = pList[i] 
            
            else:
                break 
        return lastCommon