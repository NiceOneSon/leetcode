import heapq
from collections import defaultdict

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        q = []
        nums_count_dict = defaultdict(int)
        
        for num in nums: 
            nums_count_dict[num] += 1
        
        for key, val in nums_count_dict.items():
            heapq.heappush(q, (-key, val))

        answer = 0
        while len(q) > 1:
            _, val = heapq.heappop(q)
            next_minus_key, next_val = heapq.heappop(q)
            
            answer += val
            next_val += val
            heapq.heappush(q, (next_minus_key, next_val))
        
        return answer