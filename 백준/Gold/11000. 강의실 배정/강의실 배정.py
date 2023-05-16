import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
orders = [tuple(map(int, input().split(' '))) for _ in range(N)]
orders.sort()
for S, E in orders:
    if not q:
        heapq.heappush(q, E)
    elif q[0] > S:
        heapq.heappush(q, E)
    else:
        heapq.heappop(q)
        heapq.heappush(q, E)

print(len(q))