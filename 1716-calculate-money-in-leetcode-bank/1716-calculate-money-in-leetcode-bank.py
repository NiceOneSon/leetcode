from typing import Optional

class Solution:
    
    def getTotal(self, seven_blocks: int, resid : int) -> int:
        answer = 0 
        week = -1
        for week in range(seven_blocks):
            answer += week * 7 + 7 * 8 // 2
        
        week += 1
        
        for day in range(1, resid + 1):
            answer += day + week
        return answer
    
    def totalMoney(self, n: int) -> int:
        seven_blocks = n//7
        resid = n % 7
        answer = self.getTotal(seven_blocks, resid)
        return answer