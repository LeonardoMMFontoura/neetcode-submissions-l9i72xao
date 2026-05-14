class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adj_list[u].append(v)
            indegree[v]+=1
        queue = deque([i for i in range(n) if indegree[i] == 0])
        result = []
        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)
            for neighbor_node in adj_list[curr_node]:
                indegree[neighbor_node]-=1
                if indegree[neighbor_node] == 0:
                    queue.append(neighbor_node)
        if len(result) == n:
            return result 
        else:
            return []
        