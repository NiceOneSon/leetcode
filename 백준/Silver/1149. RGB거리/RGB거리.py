N = int(input())
routes = []
for _ in range(N):
    a, b, c = map(int, input().split(' '))
    routes.append((a, b, c))


DP = [[0] * (3) for _ in range(N)]
DP[0] = routes[0]
for ind in range(1, N):
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if DP[ind][j] == 0:
                DP[ind][j] = DP[ind-1][i] + routes[ind][j]
            else:
                DP[ind][j] = min(DP[ind][j], DP[ind-1][i] + routes[ind][j])
else:
    answer = min(DP[ind])

print(answer)