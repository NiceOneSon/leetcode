from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [defaultdict(int) for _ in range(length)]
        answer = 0
        
        for i in range(length):
            for j in range(i):
                
                num = nums[i] - nums[j]
                
                dp[i][num] += dp[j][num] + 1
                answer += dp[j][num]
                
        return answer