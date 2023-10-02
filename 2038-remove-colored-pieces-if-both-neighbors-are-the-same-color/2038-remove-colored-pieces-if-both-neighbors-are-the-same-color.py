from collections import Counter

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A = []
        B = []
        for i in range(2, len(colors)):
            if colors[i] == colors[i-1] == colors[i-2]:
                if colors[i] == 'A':
                    A.append(i)
                else:
                    B.append(i)
        
        return len(A) > len(B)