class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = 0

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1
            return True
        return False

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind(rows * cols)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    uf.count += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    index_atual = r * cols + c

                    if c + 1 < cols and grid[r][c + 1] == "1":
                        uf.union(index_atual, r * cols + (c + 1))
                        
                    if r + 1 < rows and grid[r + 1][c] == "1":
                        uf.union(index_atual, (r + 1) * cols + c)
        
        return uf.count