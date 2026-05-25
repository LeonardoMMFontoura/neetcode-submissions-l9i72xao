class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0), (0,-1), (0,1)]
        min_steps = 0

        global_queue = deque()
        def bfs(start_r, start_c):
            local_queue = deque([(start_r, start_c)])
            grid[start_r][start_c] = "*"
            global_queue.append((start_r, start_c))
            while local_queue:
                r,c = local_queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = "*"
                        global_queue.append((nr, nc)) 
                        local_queue.append((nr, nc))
        def find_first_island():
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1:
                        bfs(row, col)
                        return 
        
        find_first_island()
        while global_queue:
            level_size = len(global_queue)
            for _ in range(level_size):
                r, c = global_queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < rows and 0 <= nc < cols):
                        if grid[nr][nc] == 1:
                            return min_steps
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = "*"
                            global_queue.append((nr, nc))
            min_steps+=1
        return min_steps


         

