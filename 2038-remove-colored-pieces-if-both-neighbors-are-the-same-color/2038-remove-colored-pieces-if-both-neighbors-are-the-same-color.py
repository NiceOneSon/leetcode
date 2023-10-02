from collections import Counter

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A = 0
        B = 0
        for i in range(2, len(colors)):
            if colors[i] == colors[i-1] == colors[i-2]:
                if colors[i] == 'A':
                    A += 1
                else:
                    B += 1
        
        return A > B