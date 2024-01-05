from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        DP = [1] * len(nums)
        
        for i in range(len(nums)):
            DP[i] = 1
        
        for end in range(len(nums)):
            for start in range(end):
                if nums[start] < nums[end]:
                    DP[end] = max(DP[end], DP[start] + 1)
        
        return max(DP)