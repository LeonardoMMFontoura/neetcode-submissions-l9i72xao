class UnionFind:
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank =[0] * n
        self.num_components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        elif self.rank[ry] > self.rank[rx]:
            self.parent[rx] = ry
        else:
            self.parent[rx] = ry
            self.rank[ry] +=1
        self.num_components-=1
        return True

    def getNumComponents(self) -> int:
        return self.num_components
