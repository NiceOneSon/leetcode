from bisect import bisect_right, bisect_left

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        nums = [0] + nums + [0]
        INF = float('inf')
        answer = INF
        if sum(nums) < x:
            return -1
        # 누적합.
        accLeft = [0] * len(nums)        
        for ind in range(len(nums)):
            accLeft[ind] = accLeft[ind-1] + nums[ind]
        
        accRight = [0] * len(nums)  
        accRight[-1] = nums[-1]
        for ind in range(len(nums)-2, -1, -1):
            accRight[ind] = accRight[ind+1] + nums[ind]
        
        for rightInd in range(len(nums)-1, -1, -1):
            rightNums = accRight[rightInd]
            leftInd = bisect_left(accLeft, x - rightNums)
            leftNums = accLeft[leftInd]
            if rightNums + leftNums == x:
                answer = min(answer, len(nums) - rightInd + leftInd - 1)
        
        if answer == INF:
            return -1
        return answer