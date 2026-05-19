class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        min_heap = [(0,src,0)]
        visited = set()
        while min_heap:
            curr_dist, curr_node, stops = heapq.heappop(min_heap)
            if curr_node == dst:
                return curr_dist
            if (curr_node, stops) in visited:
                continue
            visited.add((curr_node,stops))
            if stops > k:
                continue
            for neighbor, weight in graph[curr_node]:
                new_dist = weight + curr_dist
                heapq.heappush(min_heap, (new_dist, neighbor, stops+1))
        return -1