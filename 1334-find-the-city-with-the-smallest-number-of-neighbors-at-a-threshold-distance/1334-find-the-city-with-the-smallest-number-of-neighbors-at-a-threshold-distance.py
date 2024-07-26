from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf_distance: float = float('inf')
        
        neighborhoods: list[list[int]] = [[] for _ in range(n+1)]
        
        optimized_dict: dict[int, dict[int, int]] = defaultdict(lambda: defaultdict(lambda: inf_distance))
        
        for start, end, dist in edges:
            neighborhoods[start].append(end)
            neighborhoods[end].append(start)
            optimized_dict[start][end] = dist
            optimized_dict[end][start] = dist
        
        def dijkstra(start: int) -> int:
            nonlocal optimized_dict
            
            q = []
            q.append((0, start))
            visited: set = set()
                
            while q:
                moved, node = heapq.heappop(q)
                
                for end in neighborhoods[node]:
                    next_move: int = moved + optimized_dict[node][end]
                    if end == start:
                        continue
                    if next_move > distanceThreshold:
                        continue
                    if next_move > optimized_dict[start][end]:
                        continue
                    
                    optimized_dict[start][end] = next_move
                    optimized_dict[end][start] = next_move
                    
                    heapq.heappush(q, (next_move, end))
                    visited.add(end)
            return len(visited)
        
        answer_dist: float = inf_distance
        answer_node: int = 0
            
        for node in range(n):
            result: int = dijkstra(node)
            if answer_dist >= result:
                answer_dist = result
                answer_node = node
        return answer_node