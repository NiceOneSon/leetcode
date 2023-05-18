import sys
input = sys.stdin.readline

from bisect import bisect_left

seoksun, jongu = [], []

N, M = map(int, input().split(' '))
answer = [0] * (M+1)

for i in range(N):
    if i % 2:
        jongu.append(int(input()))
    else:
        seoksun.append(int(input()))

jongu.sort()
seoksun.sort()

for height in range(1, M+1):
    ind1 = bisect_left(seoksun, height)
    ind2 = bisect_left(jongu, M - height + 1)
    answer[height] += (len(seoksun) - ind1 + len(jongu) - ind2)

minval = float('inf')
result = 0
for num in answer[1:]:
    if minval > num:
        result = 1
        minval = num
    elif minval == num:
        result += 1
print(minval, result)
