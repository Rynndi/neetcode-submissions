from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # subRoot is empty, so it is always a subtree
        if subRoot is None:
            return True 
        # root is empty but subRoot is not, so impossible
        if root is None:
            return False 
        queue = deque([root])
        while queue: 
            bigNode = queue.popleft() 
            # Processing case:
            # If this big-tree node has the same value as subRoot,
            # it might be the start of the subtree.
            if bigNode.val == subRoot.val: 
                isSame = True
                subQ = deque([(bigNode, subRoot)])

                while subQ: 
                    bigCompareNode, smallNode = subQ.popleft() 
                    # both missing --> pair matches
                    if bigCompareNode is None and smallNode is None:
                        continue 
                    # one missing but not the other --> structures differ
                    if bigCompareNode is None or smallNode is None: 
                        isSame = False 
                        break 
                    # both exist but values differ --> not same tree
                    if bigCompareNode.val != smallNode.val:
                        isSame = False
                        break
                    # keep comparing left with left, right with right
                    subQ.append((bigCompareNode.left, smallNode.left))
                    subQ.append((bigCompareNode.right, smallNode.right))
                # Only return True if the full comparison worked
                if isSame == True: 
                    return True 
            # Continue searching through the big tree
            if bigNode.left:
                queue.append(bigNode.left)
            if bigNode.right:
                queue.append(bigNode.right)

        return False