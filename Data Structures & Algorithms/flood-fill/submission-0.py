class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        queue = deque([(sr,sc)])
        seen = set([(sr,sc)])
        original_color = image[sr][sc]
        image[sr][sc] = color
        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and original_color == image[nr][nc]:
                    image[nr][nc] = color
                    seen.add((nr,nc))
                    queue.append((nr,nc))
        return image 

