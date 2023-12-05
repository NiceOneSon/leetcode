class Solution:
    def numberOfMatches(self, n: int) -> int:
        # Match
        #   n // 2
        # advance
        #   
        matches = 0
        teams = 0
        answer = 0
        while n > 1:
            matches = n // 2
            isEven = True if n % 2 == 0 else False
            n = matches + (0 if isEven else 1)            
            answer += matches
            
        return answer
            