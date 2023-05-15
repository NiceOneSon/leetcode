import sys

input = sys.stdin.readline

N = int(input())

routes = tuple(map(int, input().split(' ')))

M = int(input())

DP = [[False] * (N+1) for _ in range(N+1)]

def ispendulum(left, right):
    while left < right:
        if routes[left] != routes[right]:
            return False
        left += 1
        right -= 1
    return True

for i in range(N):
    DP[i][i] = True

for i in range(N):
    for j in range(N-1, i, -1):
        left, right = i, j
        if DP[left][right]:
            continue
        if routes[left] == routes[right]:
            result = ispendulum(left, right)
            if result:
                while left < right:
                    DP[left][right] = True
                    left += 1
                    right -= 1
for _ in range(M):
    S, E = map(lambda x : int(x) - 1, input().split(' '))
    print(1 if DP[S][E] else 0)