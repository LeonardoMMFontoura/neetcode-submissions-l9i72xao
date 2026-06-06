class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.num_components = size
        self.component_size = [1] * size
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node_a, node_b):
        root_a, root_b = self.find(node_a), self.find(node_b)
        if root_a == root_b:
            return False
        if self.component_size[root_a] < self.component_size[root_b]:
            self.parent[root_a] = root_b
            self.component_size[root_b] +=self.component_size[root_a]
        else:
            self.parent[root_b] = root_a
            self.component_size[root_a]+=self.component_size[root_b]
        self.num_components-=1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        edges.sort(key=lambda e: e[2])
        edges_used = 0
        total_weight = 0
        for u,v,w in edges:
            if uf.union(u,v):
                edges_used+=1
                total_weight+=w
                if edges_used == n-1:
                    break
        return total_weight if edges_used == n-1 else -1 



