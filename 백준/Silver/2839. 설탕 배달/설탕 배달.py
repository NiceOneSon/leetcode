N = int(input())
INF = float('inf')
answer = INF

routes = [[0, 0] for i in range(N)]

for five in range(N):
    if five * 5 <= N:
        if (N - five * 5) % 3 == 0:
            answer = min(answer, five + (N - five * 5) // 3)
print(answer if answer != INF else -1)