import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split(' '))

q = []

for _ in range(N):
    weight, value = map(int, input().split(' '))
    heapq.heappush(q, (weight, value))

bags = [int(input()) for _ in range(K)]

bags.sort()

answer = 0

check = []

for bag in bags:
    while q and q[0][0] <= bag:
        heapq.heappush(check, -heapq.heappop(q)[1])
    
    if check:
        val = heapq.heappop(check)
        answer -= val
print(answer)