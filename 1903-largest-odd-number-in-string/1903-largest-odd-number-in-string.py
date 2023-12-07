class Solution:
    def largestOddNumber(self, numbers: str) -> str:
        odds = ('1', '3', '5', '7', '9')
        for idx in range(len(numbers)-1, -1, -1):
            if numbers[idx] in odds:
                return numbers[:idx+1]
        return ""
