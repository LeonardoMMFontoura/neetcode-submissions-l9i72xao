class Solution:
    class UnionFind():
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            rootX, rootY = self.find(x), self.find(y)
            if rootX == rootY:
                return False
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] +=1
            return True            

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = self.UnionFind(n)
        for u,v in edges:
            uf.union(u,v)
        count = 0
        for i in range(n):
            if uf.parent[i] == i:
                count+=1
        return count







