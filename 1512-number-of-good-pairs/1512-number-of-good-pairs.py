class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        
        for ind, val in enumerate(nums):
            d[val].append(ind)
        
        import math
        answer = 0
        for val in d.values():
            if len(val) <= 1:
                continue
            
            answer += math.comb(len(val), 2)
            
        
        return answer