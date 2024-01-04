from collections import defaultdict
from functools import lru_cache

class Solution:
    
    @lru_cache(10**5)
    def minCost(self, num):
        if num <= 1:
            return float('inf')
        if num == 2:
            return 1
        if num == 3:
            return 1
        
        answer = float('inf')
        answer = min(answer, self.minCost(num - 3) + 1)
        answer = min(answer, self.minCost(num - 2) + 1)
        return answer
    
    def minOperations(self, nums: List[int]) -> int:
        dict_cnt = defaultdict(int)
        answer = 0
        for num in nums:
            dict_cnt[num] += 1
        
        for key, val in dict_cnt.items():
            if val == 1:
                return -1
            
            answer += self.minCost(val)
        
        return answer