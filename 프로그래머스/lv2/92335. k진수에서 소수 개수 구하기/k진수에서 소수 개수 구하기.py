def solution(n, k):
    def trans(n, k):
        answer = ''
        while n:
            answer += str(n % k)
            n //= k
        return answer[::-1].split('0')
    def prime(n):
        for num in range(2, int(n**0.5)+1):
            if n % num == 0:
                return False
        return True
            
    nums = trans(n, k)
    answer = 0 
    for num in nums:
        if not num or num == '1':
            continue
        num = int(num)
        if prime(num):
            
            answer += 1
    return answer