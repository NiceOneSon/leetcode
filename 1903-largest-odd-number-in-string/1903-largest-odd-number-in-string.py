class Solution:
    def largestOddNumber(self, numbers: str) -> str:
        
        for idx in range(len(numbers)-1, -1, -1):
            if int(numbers[idx]) % 2:
                return numbers[:idx+1]
        return ""
