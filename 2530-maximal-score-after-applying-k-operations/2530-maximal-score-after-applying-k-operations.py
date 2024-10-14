import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq
        q = [-num for num in nums]
        heapq.heapify(q)
        answer = 0
        for _ in range(k):
            num = heapq.heappop(q)
            answer -= num
            heapq.heappush(q, -math.ceil(-num/3))
        return answer