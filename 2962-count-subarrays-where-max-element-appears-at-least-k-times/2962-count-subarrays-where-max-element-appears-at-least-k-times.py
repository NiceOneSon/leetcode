

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        maxnum = max(nums)
        cnt = 0
        answer = 0
                
        for right in range(len(nums)):
            if nums[right] == maxnum:
                cnt += 1
                
            while left <= right and cnt >= k:
                answer += len(nums) - right
                if nums[left] == maxnum:
                    cnt -= 1
                left += 1
            
        return answer