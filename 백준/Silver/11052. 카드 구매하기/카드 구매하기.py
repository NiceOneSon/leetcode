N = int(input())
answer = [0] * (N+1)
routes = [0] + list(map(int, input().split(' ')))

for i in range(1, N+1):
    for j in range(1, len(routes)+1):
        if i - j >= 0:
            answer[i] = max(answer[i], answer[i - j] + routes[j])
print(answer[N])