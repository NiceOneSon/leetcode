N =int(input())
prev, answer = 1, 2
if N == 1:
    print(prev)
else:
    for i in range(3, N+1):
        tmp = answer
        answer += prev
        prev = tmp
        answer %= 15746
    print(answer)
