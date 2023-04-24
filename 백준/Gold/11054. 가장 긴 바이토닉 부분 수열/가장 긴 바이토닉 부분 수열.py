N = int(input())
routes = list(map(int, input().split()))
answer = 0 
DP = [1] * N
reversed_DP = [1] * N
for i in range(1, N):
    for j in range(i):
        if routes[i] > routes[j]:
            DP[i] = max(DP[i], DP[j]+1)

routes = routes[::-1]

for i in range(1, N):
    for j in range(i):
        if routes[i] > routes[j]:
            reversed_DP[i] = max(reversed_DP[i], reversed_DP[j]+1)

for i in range(N):
    answer = max(answer, DP[i]+reversed_DP[N-1-i])
print(answer-1)