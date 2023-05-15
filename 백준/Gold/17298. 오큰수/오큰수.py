N = int(input())

left = tuple(map(int, input().split(' ')))

answer = [-1]
right = [left[-1]]
for ind in range(N-2, -1, -1):
    if right and right[-1] > left[ind]:
        answer += [right[-1]]
        right.append(left[ind])
    else:
        while right and right[-1] <= left[ind]:
            right.pop()
        else:
            if right and right[-1] > left[ind]:
                answer += [right[-1]]
                right.append(left[ind])
            else:
                answer += [-1]
                right.append(left[ind])
print(*answer[::-1])