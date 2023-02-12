N = int(input())

for _ in range(N):
    command = input()
    _ = int(input())
    result = input()

    if result == '[]':
        routes = []
    else:
        routes = list(map(int, result[1:-1].split(',')))
    left, right = 0, len(routes)
    reversed = False

    for com in command:
        if com == 'R':
            reversed = not reversed
        else:
            if not reversed:
                left += 1
            else:
                right -= 1
    if left > right:
        print('error')
    elif not reversed:
        print('[' + ','.join(map(str, routes[left:right])) + ']')
    else:
        print('[' + ','.join(map(str, routes[left:right][::-1])) + ']')
