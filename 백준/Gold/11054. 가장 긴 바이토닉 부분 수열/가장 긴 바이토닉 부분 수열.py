N = int(input())

routes = list(map(int, input().split(' ')))

DP = [1] * (len(routes)+1)
for i in range(1, len(routes)):
    for j in range(i):
        if routes[i] > routes[j]:
            DP[i] = max(DP[j]+1, DP[i])
DP_rev = [1] * (len(routes) + 1)
for i in range(len(routes)-2, -1, -1):
    for j in range(len(routes)-1, i, -1):
        if routes[i] > routes[j]:
            DP_rev[i] = max(DP_rev[j]+1, DP_rev[i])
answer = 0 
for i in range(len(routes)):
    answer = max(answer, DP[i] + DP_rev[i] - 1)
print(answer)