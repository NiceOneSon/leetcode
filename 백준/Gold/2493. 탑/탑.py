N = int(input())

routes = tuple(map(int, input().split(' ')))

stack = [(0, routes[0])]

answer = [0]
for i in range(1, len(routes)):
    tower = routes[i]
    while stack and stack[-1][1] < tower:
        stack.pop()
    if stack:
        answer.append(stack[-1][0] + 1)
    else:
        answer.append(0)
    stack.append((i, tower))
print(*answer)