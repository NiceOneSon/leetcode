from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split(' '))
ingress = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split(' '))
    graph[A].append(B)
    ingress[B] += 1
q = deque()
for i in range(1, N+1):
    if ingress[i] == 0:
        q.append(i)
answer = []
while q:
    num = q.popleft()
    answer.append(num)
    for nextnum in graph[num]:
        ingress[nextnum] -= 1
        if ingress[nextnum] == 0:
            q.append(nextnum)
print(*answer)