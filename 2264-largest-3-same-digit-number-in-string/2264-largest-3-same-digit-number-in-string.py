class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = ''
        for idx in range(2, len(num)):
            if num[idx-2] == num[idx-1] and num[idx-1] == num[idx]:
                number = num[idx-2:idx+1]
                answer = max(answer, number)
        return answer