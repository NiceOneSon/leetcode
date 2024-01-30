import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        answer = 0
        
        def calc(nums, char):
            right = nums.pop()
            left = nums.pop()
            if char == '+':
                return left + right
            elif char == '-':
                return left - right
            elif char == '*':
                return left * right
            sign = (left >= 0 and right >= 0 or left < 0 and right < 0)
            if sign:
                return left // right
            return -math.floor(-left // right)
        
        for char in tokens:
            if char in '+-*/':
                num = calc(nums, char)
            else:
                num = int(char)
            nums.append(num)
        return nums[0]
    

    