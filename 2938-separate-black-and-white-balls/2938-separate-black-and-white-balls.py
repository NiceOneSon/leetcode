class Solution:    
    def minimumSteps(self, s: str) -> int:
        stack = []
        idx = len(s) - 1
        t_cnt = s.count('1')
        answer = 0
        
        for _ in range(t_cnt):
            while s[idx] == '0':
                stack.append(True)
                idx -= 1
            answer += len(stack)
            idx -= 1
            
        return answer
            