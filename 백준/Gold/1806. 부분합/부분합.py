n, s = map(int, input().split(' '))

routes = list(map(int, input().split(' ')))

cumsum = 0
answer = float('inf')
left, right = 0, 0
while right < n:
    cumsum += routes[right]
    right += 1
    if cumsum >= s:
        while cumsum >= s and left < right:
            answer = min(answer, right - left)
            cumsum -= routes[left]
            left += 1
print(answer if answer != float('inf') else 0)
    