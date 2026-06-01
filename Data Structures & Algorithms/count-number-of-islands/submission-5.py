class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.component_size = [1] * size
        self.num_components = size
    
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
            self.component_size[root_b]+=self.component_size[root_a]
        else:
            self.parent[root_b] = root_a
            self.component_size[root_a]+=self.component_size[root_b]
        self.num_components-=1
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind(rows * cols)
        
        # 2. Como sua classe começa contando água ("0") como componentes,
        # precisamos descobrir quantas águas existem para sintonizar o num_components.
        total_water = 0
        
        # Olhamos apenas para Direita e Baixo para evitar uniões redundantes
        directions = [(1, 0), (0, 1)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    total_water += 1
                else:
                    current_node = r * cols + c
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            neighbor_node = nr * cols + nc
                            uf.union(current_node, neighbor_node)
                            
        # 3. O resultado final de ilhas será: 
        # (Componentes totais do UF) - (Células de água que o UF achou que eram componentes)
        return uf.num_components - total_water


        