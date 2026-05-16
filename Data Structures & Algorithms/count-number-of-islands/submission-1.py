class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        islands = 0

        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = "*"
            while queue:
                row, col  = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "*"
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands+=1
        return islands