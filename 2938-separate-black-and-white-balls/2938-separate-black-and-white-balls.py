class Solution:    
    def minimumSteps(self, s: str) -> int:
        zero_cnt = 0
        idx = len(s) - 1
        # t_cnt = s.count('1')
        answer = 0
        
        # for _ in range(t_cnt):
        while True:
            while idx >= 0 and s[idx] == '0':
                zero_cnt += 1
                idx -= 1
            if idx < 0:
                return answer
            answer += zero_cnt
            idx -= 1
            
        return answer
            