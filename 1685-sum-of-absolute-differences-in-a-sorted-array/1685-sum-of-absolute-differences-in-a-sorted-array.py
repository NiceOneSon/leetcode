class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        rightSum = [nums[-1]]
        leftSum = [nums[0]]
        
        for numIdx in range(len(nums)-2, -1, -1):
            num = nums[numIdx]
            rightSum.append(rightSum[-1] + num)
        rightSum = rightSum[::-1]
        
        for numIdx in range(1, len(nums)):
            num = nums[numIdx]
            leftSum.append(leftSum[-1] + num)
        
        answer = []
        for numIdx in range(len(nums)):
            num = 0
            if numIdx > 0:
                tmpLeft = nums[numIdx] * numIdx
                tmpLeft -= leftSum[numIdx-1]
                num += tmpLeft
            if numIdx < len(nums) - 1:
                tmpRight = rightSum[numIdx+1]
                tmpRight -= nums[numIdx] * (len(nums) - numIdx - 1)
                num += tmpRight
            answer.append(num)
        
        return answer