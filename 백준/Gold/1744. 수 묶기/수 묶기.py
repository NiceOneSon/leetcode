N = int(input())
plus, minus, zeros = [], [], 0
for _ in range(N):
    num = int(input())
    if num > 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    else:
        zeros += 1

plus.sort()
minus.sort(reverse=True)
answer = 0

while plus:
    num1 = plus.pop()
    if plus:
        num2 = plus.pop()
        answer += max(num1 * num2, num1 + num2)
    else:
        answer += num1

while minus:
    num1 = minus.pop()
    if minus:
        num2 = minus.pop()
        answer += max(num1 * num2, num1 + num2)
    else:
        if zeros:
            answer += 0
        else:
            answer += num1

print(answer)
    