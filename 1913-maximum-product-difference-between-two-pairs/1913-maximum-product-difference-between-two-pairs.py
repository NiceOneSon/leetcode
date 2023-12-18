class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        import heapq
        
        minq, maxq = [], []
        
        for num in nums:
            heapq.heappush(minq, -num)
            heapq.heappush(maxq, num)
            
            if len(minq) > 2:
                heapq.heappop(minq)
                heapq.heappop(maxq)
                
        return maxq[0] * maxq[1] - minq[0] * minq[1]
            