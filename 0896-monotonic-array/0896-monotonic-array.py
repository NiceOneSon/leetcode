class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        s1 = sorted(nums)
        s2 = sorted(nums, reverse = True)
        
        if s1 == nums:
            return True
        if s2 == nums:
            return True
        return False