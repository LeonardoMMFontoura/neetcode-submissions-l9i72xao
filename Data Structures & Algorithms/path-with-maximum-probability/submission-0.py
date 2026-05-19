class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u,v) in enumerate(edges):
            prob = succProb[i]
            graph[u].append((v,prob))
            graph[v].append((u,prob))
        distances = {node: 0 for node in range(n)}
        distances[start_node] = 1
        max_heap = [(-1, start_node)]
        while max_heap:
            curr_dist, curr_node = heapq.heappop(max_heap)
            curr_dist = -curr_dist
            if curr_dist < distances[curr_node]:
                continue
            for neighbor, weight in graph[curr_node]:
                new_dist = weight * curr_dist
                if new_dist > distances[neighbor]:
                    distances[neighbor] = new_dist 
                    heapq.heappush(max_heap, (-new_dist, neighbor))
        return distances[end_node]
        
