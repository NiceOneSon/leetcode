class Solution:
    def reverse(self, x: int) -> int:
        sign = True if x >= 0 else False
        if sign:
            answer = ''
        else:
            answer = '-'
            x *= -1
        
        cnt =0 
        while x:
            if cnt == 10:
                break
                
            cnt += 1
            num = x % 10
            if num or answer:
                answer += str(num)
            x //= 10
        if not answer:
            return 0
        
        answer = int(answer)
        if (1 << 31) > answer and -(1 << 31) < answer:
            return answer
        else:
            return 0
        