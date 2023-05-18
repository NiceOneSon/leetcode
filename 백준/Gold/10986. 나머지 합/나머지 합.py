import math
answer = 0

N, M = map(int, input().split(' '))

nums = tuple(map(int, input().split(' ')))

routes = [0] * (N+1)

for i in range(N):
    routes[i+1] += nums[i] + routes[i]
    routes[i+1] %= M

dic = {}
for num in routes:
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

for val in dic.values():
    answer += math.comb(val, 2)
print(answer)