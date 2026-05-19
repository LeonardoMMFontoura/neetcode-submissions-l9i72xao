class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        distances = {node: float("inf") for node in range(1, n+1)}
        distances[k] = 0
        min_heap = [(0,k)]  
        while min_heap:
            curr_dist, curr_node = heapq.heappop(min_heap)
            if curr_dist > distances[curr_node]:
                continue
            for neighbor, weight in graph[curr_node]:
                new_dist = weight + curr_dist
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(min_heap,(new_dist, neighbor))
        max_distance = max(distances.values())
        return -1 if max_distance == float("inf") else max_distance
