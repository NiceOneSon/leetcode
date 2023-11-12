from collections import deque, defaultdict
import heapq

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        q = []
        bus_routes = defaultdict(list)
        answer = float('inf')
        duplicated = defaultdict(lambda : float('inf'))
        duplicated[source] = 0
        
        for bus, route in enumerate(routes, start = 1):
            if len(route) == 1:
                continue
            for i in range(len(route)):
                node = route[i]
                nextnode = route[i-1]
                bus_routes[node].append((nextnode, bus))
        
        for node, bus in bus_routes[source]:
            heapq.heappush(q , (1, bus, node))
            duplicated[node] = 1
            if node == target:
                return 1
        while q:
            cnt, bus, node = heapq.heappop(q)
            
            if cnt >= answer:
                continue
            if node == target:
                return cnt
            for nextnode, nextbus in bus_routes[node]:
                if bus != nextbus:
                    if duplicated[nextnode] < cnt+1:
                        continue
                    heapq.heappush(q, (cnt+1, nextbus, nextnode))
                    duplicated[nextnode] = cnt+1
                else:
                    if duplicated[nextnode] < cnt:
                        continue
                    heapq.heappush(q, (cnt, nextbus, nextnode))
                    duplicated[nextnode] = cnt
        return answer if answer != float("inf") else -1
                    