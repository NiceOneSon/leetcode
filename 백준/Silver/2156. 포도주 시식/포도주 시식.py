N = int(input())
DP = [[0] * N for _ in range(3)]
routes = []

for _ in range(N):
    number = int(input())
    routes.append(number)

DP[1][0] = routes[0]

for ind in range(1, N):
    DP[0][ind] = max(DP[0][ind-1], DP[1][ind-1], DP[2][ind-1])
    DP[1][ind] = DP[0][ind-1] + routes[ind]
    DP[2][ind] = DP[1][ind-1] + routes[ind]

answer = 0
for i in range(3):
    answer = max(answer, max(DP[i]))
print(answer)