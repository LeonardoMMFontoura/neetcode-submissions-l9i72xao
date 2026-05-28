class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        adj_list = defaultdict(list)
        for bus, stop in enumerate(routes):
            for stop in stop:
                adj_list[stop].append(bus)
        queue = deque([(source, 0)])
        buses_taken = set()
        while queue:
            curr_stop, num_buses = queue.popleft()
            if curr_stop == target:
                return num_buses
            for bus in adj_list[curr_stop]:
                if bus not in buses_taken:
                    buses_taken.add(bus)
                    for next_stop in routes[bus]:
                        queue.append((next_stop, num_buses + 1))
        return -1
         

