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
        hashmap[node] = Node(node.val)
        stack = [node]
        visited = set() 
        while stack: 
            currNode = stack.pop()
            if currNode in visited: 
                continue 
            visited.add(currNode)
            for neighbor in currNode.neighbors:
                if neighbor not in hashmap:
                    hashmap[neighbor] = Node(neighbor.val)
                hashmap[currNode].neighbors.append(hashmap[neighbor])
              
                if neighbor not in visited:
                    stack.append(neighbor)

        return hashmap[node]
            
            


        