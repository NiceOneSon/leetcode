N = int(input())

routes = [tuple(map(int, input().split(' '))) for _  in range(N)]

routes.sort()

routes = tuple(map(lambda x : x[1], routes))

DP = [0] * N

for i in range(N):
    DP[i] = 1
    for j in range(i):
        if routes[j] < routes[i]:
            DP[i] = max(DP[i], DP[j] + 1)

print(N - max(DP))