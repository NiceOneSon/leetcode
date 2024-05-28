class Solution:
    
    def getstringDiff(self, s: str, t: str) -> list[int]:
        def charDiff(chars: str, chart: str) -> int:
            return abs(ord(chars) - ord(chart))
        answer = []
        length = len(s)
        for idx in range(length):
            answer.append(charDiff(s[idx], t[idx]))
        return answer
    
        
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length = len(s)
        
        def getMaxLengthUsingTwoPointer(diff_list):
            left = 0
            cnt = 0
            answer = 0
            for right in range(length):
                cnt += diff_list[right]
                
                while cnt > maxCost and left < right:
                    cnt -= diff_list[left]
                    left += 1
                if cnt <= maxCost:
                    answer = max(answer, right - left + 1)
            return answer
            
        diff_list: list[int] = self.getstringDiff(s, t)
        
        return getMaxLengthUsingTwoPointer(diff_list)