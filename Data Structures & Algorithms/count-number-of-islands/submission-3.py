class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        islands = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "*"
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr,nc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands+=1
        return islands
         
