import heapq

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        q = []
        for coin in piles:
            heapq.heappush(q, -coin)
            
        answer = 0
        length = len(q)
        while length >= 3:
            _ = heapq.heappop(q)
            me = heapq.heappop(q)
            length -= 3
            answer -= me
        
        return answer