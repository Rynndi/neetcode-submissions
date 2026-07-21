class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc 
                    
                    #stay inside the grid:
                    if nr <0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue 
                    if (nr, nc) in visited:
                        continue 
                    if heights[nr][nc] < heights[row][col]:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        pacificQueue = deque() 
        atlanticQueue= deque() 

        pacificVisited = set() 
        atlanticVisited = set() 

        for row in range(ROWS):
            pacificQueue.append((row, 0))
            pacificVisited.add((row, 0))
            atlanticQueue.append((row, COLS-1))
            atlanticVisited.add((row, COLS-1))

        for col in range(COLS):
            pacificQueue.append((0, col))
            pacificVisited.add((0, col))
            atlanticQueue.append((ROWS-1, col))
            atlanticVisited.add((ROWS-1, col))
        bfs(pacificQueue, pacificVisited)
        bfs(atlanticQueue, atlanticVisited)

        both = []

        for row in range(ROWS):
            for col in range(COLS):
                if ((row, col) in pacificVisited and (row, col) in atlanticVisited):
                    both.append([row, col])
        return both


        
        
        