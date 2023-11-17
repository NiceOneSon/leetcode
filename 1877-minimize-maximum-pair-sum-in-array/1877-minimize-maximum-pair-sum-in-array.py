class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        answer = 0
        while left < right:
            answer = max(answer, nums[left] + nums[right])
            left += 1
            right -= 1
        return answer