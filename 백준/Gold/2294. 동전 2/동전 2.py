n, k = map(int, input().split(' '))

INF = float('inf')
values = [INF] * 10001 # y : coin, x : value
coins = set()

for _ in range(n):
    coin = int(input())
    coins.add(coin)
    if coin > k:
        continue
    values[coin] = 1

for value in range(1, len(values)):
    for coin in coins:
        if value + coin > k:
            continue
        values[value + coin] = min(values[value + coin], values[value] + 1)

if values[k] != INF:
    print(values[k])
else:
    print(-1)