class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        import heapq
        q = []
        
        for i in range(len(dist)):
            time = (dist[i]-1)//speed[i]
            heapq.heappush(q, time)
        
        time = 0
        # print(q)
        while q and time <= q[0]:
            heapq.heappop(q)
            time += 1
        return time