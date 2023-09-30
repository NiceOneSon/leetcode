class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minDP = list(accumulate(nums, min))
        stack = []

        for i in range(len(nums)-1, -1, -1):
            if minDP[i] < nums[i]:
                while stack and stack[-1] <= minDP[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    print(stack[-1], nums[i], minDP[i])
                    return True
                stack.append(nums[i])

        return False