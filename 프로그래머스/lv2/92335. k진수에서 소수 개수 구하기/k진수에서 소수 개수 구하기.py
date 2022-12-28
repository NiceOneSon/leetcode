def solution(n, k):
    transformed = ''
    while n:
        tmp = str(n % k)
        transformed = tmp + transformed
        n //= k
    left = 0
    def check(num):
        if num == 1:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    answer = 0
    for num in transformed.split('0'):
        if not num:
            continue
        if check(int(num)) == False:
            print(num)
            answer += 1
    return answer