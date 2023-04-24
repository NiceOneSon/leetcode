N = int(input())
routes = list(map(int, input().split(' ')))
DP = [1] * (N)
for i in range(1, N):
    for j in range(i):
        if routes[i] > routes[j]:
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))