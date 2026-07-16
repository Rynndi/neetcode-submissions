class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islandCount = 0 

        def bfs(r, c):
            queue = deque() 
            #equivalent of visited set, but just mark as 0 
            grid[r][c] = "0"
            queue.append((r,c))

            while queue:
                row, col = queue.popleft() 
                for dr, dc in directions: 
                    nr, nc = dr + row, dc + col 
                    if nr >= ROWS or nc >= COLS or nr < 0 or nc < 0 or grid[nr][nc] == "0": 
                        continue 
                    queue.append((nr, nc))
                    grid[nr][nc] = "0" 

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] =="1":
                    bfs(row,col)
                    islandCount+=1 
        return islandCount 



        