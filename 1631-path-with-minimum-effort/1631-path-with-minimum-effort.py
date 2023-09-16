from collections import defaultdict
import heapq

class Solution:
    def dijkstra(self, y, x, heights):
        ly, lx = len(heights), len(heights[0])
        dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
        distance = defaultdict(lambda : float('inf'))
        distance[(y, x)] = 0
        q = []
        heapq.heappush(q, (y, x, distance[(y, x)]))
        
        while q:
            y, x, cost = heapq.heappop(q)
            for i in range(4):
                sy, sx = y + dy[i], x + dx[i]
                if not (0<=sy<ly and 0<=sx<lx):
                    continue
                
                if distance[(sy, sx)] > max(cost, abs(heights[sy][sx] - heights[y][x])):
                    distance[(sy, sx)] = max(cost, abs(heights[sy][sx] - heights[y][x]))
                    heapq.heappush(q, (sy, sx, distance[(sy, sx)]))
        return distance[(ly-1, lx-1)]
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        return self.dijkstra(0, 0, heights)
        