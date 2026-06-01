class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        num_islands = 0

        def bfs(start_r, start_c):
            if not grid:
                return 0
            queue = deque([(start_r, start_c)])
            grid[start_r][start_c] = "*"
            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):
                        queue.append([nr,nc])
                        grid[nr][nc] = "*"
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row,col)
                    num_islands+=1
        return num_islands