class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(0,1),(0,-1),(-1,0)]

        def dfs(r,c):
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                return 0
            count = 1
            grid[r][c] = "*" 
            for dr,dc in directions:
                nr,nc = dr + r, dc + c
                count+=dfs(nr,nc)
            return count

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, dfs(row,col)) 
        return max_area 
