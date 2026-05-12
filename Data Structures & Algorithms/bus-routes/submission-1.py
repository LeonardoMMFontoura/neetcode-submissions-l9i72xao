class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = defaultdict(set)
        stop_list = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_list[stop].append(bus)
        for bus in range(len(routes)):
            for stop in routes[bus]:
                for other_bus in stop_list[stop]:
                    if other_bus != bus:
                        adj[bus].add(other_bus)
        if target == source:
            return 0
        queue = deque()
        seen = set()
        for bus in stop_list[source]:
            queue.append((bus, 1))
            seen.add(bus)
        while queue:
            curr_bus, num_buses = queue.popleft()
            if target in routes[curr_bus]:
                return num_buses
            for next_bus in adj[curr_bus]:
                if next_bus not in seen:
                    seen.add(next_bus)
                    queue.append((next_bus, num_buses + 1))
        return -1







