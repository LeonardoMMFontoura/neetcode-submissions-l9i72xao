class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.numComponents = n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node_a, node_b):
        root_node_a, root_node_b = self.find(node_a), self.find(node_b)
        if root_node_a == root_node_b:
            return False
        if self.rank[root_node_a] > self.rank[root_node_b]:
            self.parent[root_node_b] = root_node_a
        elif self.rank[root_node_a] < self.rank[root_node_b]:
            self.parent[root_node_a] = root_node_b
        else:
            self.parent[root_node_a] = root_node_b
            self.rank[root_node_b] +=1
        self.numComponents-=1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        uf = UnionFind(n)
        for u,v in edges:
            if not uf.union(u,v):
                return False
        return uf.numComponents == 1
                


            





