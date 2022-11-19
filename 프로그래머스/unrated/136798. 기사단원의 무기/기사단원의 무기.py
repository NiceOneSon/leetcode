def solution(numbers, limit, power):
    def get_num(number):
        cnt = 0
        for i in range(1, int(number**0.5) + 1):
            if number % i == 0:
                if i ** 2 == number:
                    cnt += 1
                else:
                    cnt += 2
        return cnt
    answer = 0
    for number in range(1, numbers+1):
        result = get_num(number)
        if result <= limit:
            answer += result
        else:
            answer += power
    return answer