class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #connected component: separate, disconnected subgraph. 
        #each vertex can reach every other vertex through a sequence of edges. 
        #no edges connect vertices from one component to another. 
        #cycles are allowed. 

        adj = [[] for i in range(n)]

        for source, des in edges: 
            adj[source].append(des)
            adj[des].append(source)
       
        
        visited = set() 
        count =0 

        for node in range(n):
            #process node here, has a connection. 
            if node in visited:
                continue 
            count+=1 
            stack = [node]

            while stack:
                node = stack.pop() 
                if node in visited:
                    continue 
                visited.add(node)
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return count

        

        