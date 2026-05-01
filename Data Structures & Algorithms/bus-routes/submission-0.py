class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_buses = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id) 
        # A fila guarda tuplas de (quantidade_de_onibus, parada_atual)
        queue = deque([(0, source)])
        visited_stops = {source}
        visited_buses = set()
        while queue: 
            buses_taken, current_stop = queue.popleft()
        # 🚌 Verificamos todos os ônibus que passam na parada onde estamos 
            for bus_id in stop_to_buses[current_stop]:
                if bus_id not in visited_buses:
                    visited_buses.add(bus_id)
                # 📍 Verificamos todas as paradas que este ônibus alcança
                for next_stop in routes[bus_id]:
                    if next_stop == target:
                        return buses_taken + 1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((buses_taken + 1, next_stop))
        return -1