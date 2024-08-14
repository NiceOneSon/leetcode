from bisect import bisect_left

class Solution:
    def get_result(self, number: int, nums: List[int]) -> int:
        left = 0
        lenght = len(nums)
        answer: int = 0
        for right in range(1, lenght):
            while nums[right] - nums[left] > number:
                left += 1
            answer += right - left
        return answer
        
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left, right = 0, max(nums) - min(nums)
        
        while left < right:
            number = (left + right) // 2 # distance
            result = self.get_result(number = number, nums = nums) #
            if result < k:
                left = number + 1
            else:
                right = number
        return left