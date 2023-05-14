N = int(input())

routes = list(map(int , input().split(' ')))
DP = [0] * N
for i in range(1, N):
    for j in range(i):
        if routes[i] > routes[j]:
            DP[i] = max(DP[i], DP[j] + 1)


length = max(DP)
answer = []
for i in range(N-1, -1, -1):
    if DP[i] == length:
        answer.append(routes[i])
        length -= 1
print(len(answer))
print(*answer[::-1])
