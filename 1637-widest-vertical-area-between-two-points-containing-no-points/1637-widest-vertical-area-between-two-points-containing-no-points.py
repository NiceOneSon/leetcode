class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        
        answer = 0
        prev_x = None
        for x, y in points:
            if prev_x == None:
                prev_x = x
                continue
            answer = max(answer, x - prev_x )
            prev_x = x
            
        return answer