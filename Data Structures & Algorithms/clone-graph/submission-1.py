"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None 

        hashmap = {} 
        #clone the first node 
        hashmap[node] = Node(node.val)
        
        #push it onto the stack 
        stack = [node]
        visited = set() 

        while stack: 
            #currNode is the current Node processed from the hashmap 
            currNode = stack.pop()
            
            if currNode in visited: 
                continue 
            visited.add(currNode)

        
            #problem specific work: for this one, we want to add the adjacent neighbors. 
            currClone = hashmap[currNode]

            for neighbor in currNode.neighbors:
                if neighbor not in hashmap:
                    #assign neigbor -> neighbor clone 
                    hashmap[neighbor] = Node(neighbor.val)
                    #add neighbor into the stack 
                    stack.append(neighbor)
                
                
                neighborClone = hashmap[neighbor]
                currClone.neighbors.append(neighborClone)

                if neighbor not in visited:
                    stack.append(neighbor)

    
        #returns only that one value. 
        return hashmap[node]
            
            


        