class Solution:
    
    def validate(self, number: str) -> bool:
        if not number:
            return False
        if number[0] == '0':
            return False
        if int(number) > 26:
            return False
        return True
    

    def numDecodings(self, s: str) -> int:
        length = len(s)
        
        DP = [[0] * (length) for _ in range(3)]
        
        if not self.validate(s[0]):
            return 0
        
        DP[1][0] = 1
        # DP[2][0] = 1
        
        for idx in range(1, length):
            if s[idx] != '0':
                DP[1][idx] = DP[1][idx-1] + DP[2][idx-1]
            
            if self.validate(s[idx-1:idx+1]):
                DP[2][idx] = DP[1][idx-1]
        
        return DP[1][-1] + DP[2][-1]