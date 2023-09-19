import math
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        curr = nums[0]
        for next in nums[1:]:
            if curr == next:
                return next
            curr = next