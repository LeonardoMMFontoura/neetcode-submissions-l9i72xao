class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.numComponents = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        elif self.rank[ry] > self.rank[rx]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            self.rank[rx] +=1
        self.numComponents-=1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                xi,yi = points[i]
                xj,yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append([i,j,dist])
        edges.sort(key=lambda e: e[2])
        uf = UnionFind(n)
        max_weight = 0
        used_edges = 0
        for u,v,w in edges:
            if uf.union(u,v):
                max_weight+=w
                used_edges+=1
            if used_edges == len(edges)-1:
                break
        return max_weight