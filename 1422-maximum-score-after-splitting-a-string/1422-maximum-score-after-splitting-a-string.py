class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = s.count("1")
        answer = 0
        for idx in range(len(s)-1):
            string = s[idx]
            if string == '0':
                left += 1
            else:
                right -= 1
            answer = max(answer, left + right)
            
            
        return answer