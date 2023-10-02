from collections import Counter

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A = 0
        B = 0
        for i in range(2, len(colors)):
            if colors[i-2:i+1] == 'AAA':
                A += 1
            elif colors[i-2:i+1] == 'BBB':
                B += 1
        
        return A > B