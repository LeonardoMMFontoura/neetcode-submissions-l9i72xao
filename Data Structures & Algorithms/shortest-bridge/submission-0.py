class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0), (0,-1), (0,1)]

        def find_first_island():
            island_cells = []
            queue = deque()
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1:
                        grid[row][col] = "*"
                        queue.append((row,col))
                        island_cells.append((row, col))
                        while queue:
                            r,c = queue.popleft()
                            for dr, dc in directions:
                                nr, nc = dr + r, dc + c
                                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                    grid[nr][nc] = "*"
                                    queue.append((nr,nc))
                                    island_cells.append((nr,nc))
                        return island_cells
        island_cells = find_first_island()
        distance = 0
        queue = deque(island_cells)
        while queue:
            level = len(queue)
            for _ in range(level):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            return distance
                        if grid[nr][nc] == 0:  
                            grid[nr][nc] = "*"
                            queue.append((nr, nc))
            distance+=1
        return -1




