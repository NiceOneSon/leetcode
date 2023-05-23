T = int(input())
for _ in range(T):
    N = int(input())
    routes = [list(map(int, input().split(' '))) for _ in range(2)]
    DP = [[0] * (N+1) for _ in range(2)]

    for i in range(N):
        DP[1][i] = DP[0][i-1] + routes[1][i]
        DP[0][i] = DP[1][i-1] + routes[0][i]
        if i >= 2:
            DP[1][i] = max(DP[1][i], routes[1][i] + DP[1][i-2], routes[1][i] + DP[0][i-2])
            DP[0][i] = max(DP[0][i], routes[0][i] + DP[0][i-2], routes[0][i] + DP[1][i-2])
    print(max(max(DP[1]), max(DP[0])))