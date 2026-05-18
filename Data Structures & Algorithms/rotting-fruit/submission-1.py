class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows , cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        target_count = 0
        minutes = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    target_count +=1
        if target_count == 0:
            return 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        target_count -=1
            if queue:
                minutes+=1
        return minutes if target_count == 0 else -1 