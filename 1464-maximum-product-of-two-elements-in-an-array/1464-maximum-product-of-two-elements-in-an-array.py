import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, num)
            if len(q) > 2:
                heapq.heappop(q)
        
        answer = (q[0]-1) * (q[1]-1)
        return answer