class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]

        def dfs(r,c,visited, prev_height):
            if not (0 <= r < rows and 0 <= c < cols and (r,c) not in visited and heights[r][c] >= prev_height):
                return
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = dr + r, dc + c
                dfs(nr,nc,visited,heights[r][c])
            return

        pacific = set()
        atlantic = set()

        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])

        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows-1, j, atlantic, heights[rows-1][j])
        
        #return list(pacific & atlantic)
        return [[r, c] for r, c in pacific if (r, c) in atlantic]
