class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #graphs can allow for cycles. Trees cannot. Trees also only have one root node.
        #indegrees: the number of incoming edges pointing to that vertex. 
        #a tree not only does not allow for cycles, but is only allowed one slot (node) that is 0. 
        
        #toposort is made for directed graphs. But the problem gives an undirected edge. 
        #instead, use leaf peeling: degree[node] = number of neighbors 
        if len(edges) != n-1:
            return False 

        degree = [0] * n

        adj = [[] for i in range(n)]

        for source, destination in edges:
            adj[source].append(destination) 
            adj[destination].append(source) 
            degree[source] +=1 
            degree[destination] +=1 
        


        queue = deque() 

        #leaves have degree 1. Single isolated nodes have degree 0. 
        for node in range(n):
            if degree[node] <= 1:
                queue.append(node) 
        
        topoOrder = []
        removed = set() 

        while queue: 
            node = queue.popleft()
            
            if node in removed:
                continue
            
            removed.add(node)
            topoOrder.append(node)

            for neighbor in adj[node]:
                if neighbor not in removed:
                    degree[neighbor]-=1 

                if degree[neighbor] == 1:
                    queue.append(neighbor)
            
        if len(topoOrder) == n:
            return True 
        else: 
            return False 