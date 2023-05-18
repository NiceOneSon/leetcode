import math 

T = int(input())

N = int(input())
routes1 = tuple(map(int, input().split(' ')))
sum1 = [0] * (N+1)

M = int(input())
routes2 = tuple(map(int, input().split(' ')))
sum2 = [0] * (M+1)

# prefix sum
for i in range(N):
    sum1[i+1] = sum1[i] + routes1[i]
for i in range(M):
    sum2[i+1] = sum2[i] + routes2[i]

# cases
case1 = dict()
case2 = dict()

for i in range(N):
    for j in range(i+1, N+1):
        tot = sum1[j] - sum1[i]
        if tot not in case1:
            case1[tot] = 1
            continue
        case1[tot] += 1


for i in range(M):
    for j in range(i+1, M+1):
        tot = sum2[j] - sum2[i]
        if tot not in case2:
            case2[tot] = 1
            continue
        case2[tot] += 1
answer = 0
for key1, val1 in case1.items():
    diff = T - key1
    if diff in case2:
        val2 = case2[diff]
        answer += val1 * val2
print(answer)