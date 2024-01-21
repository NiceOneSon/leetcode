class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import lru_cache
        
        @lru_cache(100)
        def recursive(ind):
            if ind >= len(nums):
                return 0
            
            answer = 0 
            answer = max(answer, recursive(ind+2) + nums[ind])
            answer = max(answer, recursive(ind+1))
            return answer
            
        return recursive(0)