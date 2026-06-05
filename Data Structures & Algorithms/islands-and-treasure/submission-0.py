class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col)) 

        while queue:
            level_size = len(queue)
            r,c = queue.popleft()
            for dr, dc in directions:
                nr,nc = dr + r, dc + c
                if (0 <= nr < rows and 0 <= nc < cols and  grid[nr][nc] == 2147483647): 
                    queue.append((nr,nc)) 
                    grid[nr][nc] = grid[r][c] + 1

    