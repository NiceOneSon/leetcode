import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    num = int(input())
    heapq.heappush(q, (num))

answer = 0 
while len(q) > 1:
    num1, num2 = heapq.heappop(q), heapq.heappop(q)
    num = num1 + num2
    heapq.heappush(q, (num))
    answer += num

print(answer)