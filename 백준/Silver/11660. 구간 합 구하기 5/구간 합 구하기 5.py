from functools import lru_cache
import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

routes = [[0] * (N+1)]

for _ in range(N):
    row = input().split(' ')
    if not row[-1]:
        row.pop()
    row = [0] + list(map(int, row))
    routes.append(row)

for y in range(1, N+1):
    for x in range(1, N+1):
        routes[y][x] += routes[y][x-1]

for y in range(1, N+1):
    for x in range(1, N+1):
        routes[y][x] += routes[y-1][x]


for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split(' '))
    print(routes[y2][x2] - routes[y1-1][x2] - routes[y2][x1-1] + routes[y1-1][x1-1])