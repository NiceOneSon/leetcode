T = int(input())
for i in range(T):
    number1, number2 = map(int, input().split(' '))
    number = number2 - number1
    maxnum = int(number ** 0.5)
    answer = maxnum + (maxnum - 1)
    number -= maxnum * (maxnum + 1) // 2 + (maxnum-1) * maxnum // 2

    while number:
        if number >= maxnum:
            answer += number // maxnum
            number %= maxnum
        maxnum -= 1
    print(answer)
        