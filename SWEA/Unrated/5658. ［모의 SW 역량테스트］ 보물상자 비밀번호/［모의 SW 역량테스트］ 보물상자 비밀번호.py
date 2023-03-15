T = int(input())
for num in range(1, T+1):
    N, K = map(int, input().split(' '))
    routes = set()
    string = input()
    length = N // 4
    string += string[:length]
    for i in range(len(string)-length):
        routes.add(string[i:i+length])
    result = list(routes)
    result.sort(reverse = True)
    print(f'#{num} {int(result[K-1], 16)}')