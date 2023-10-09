from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        leftIndex = bisect_left(nums, target)
        rightIndex = bisect_right(nums, target)
        
        if leftIndex >= len(nums) or nums[leftIndex] != target:
            return [-1, -1]
        return [leftIndex, rightIndex-1]