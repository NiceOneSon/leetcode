import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq
        
        q = [-num for num in nums]
        heapq.heapify(q)
        answer = 0
        
        while k:
            minus_num = heapq.heappop(q)
            num = -minus_num
            answer += num
            heapq.heappush(q, -math.ceil(num/3))
            k -= 1
        return answer