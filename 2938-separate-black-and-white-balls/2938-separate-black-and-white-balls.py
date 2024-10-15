class Solution:    
    def minimumSteps(self, s: str) -> int:
        l, r = len(s)-1, len(s)-1
        answer = 0 
        s = list(s)
        
        while l > 0:
            while r >= 0 and s[r] == '1':
                r -= 1
            
            while l >= 0 and (l >= r or s[l] == '0'):
                l -= 1

            if l < 0:
                return answer
            
            answer += r - l
            s[l], s[r] = s[r], s[l]
        return answer