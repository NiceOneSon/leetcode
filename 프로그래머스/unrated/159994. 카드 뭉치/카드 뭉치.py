def solution(cards1, cards2, goal):
    answer = ''
    i, j = 0, 0
    for k in range(len(goal)):
        if goal[k] == cards1[i]:
            i += 1
            i = min(i, len(cards1)-1)
        elif goal[k] == cards2[j]:
            j += 1
            j = min(j, len(cards2)-1)
        else:
            return 'No'
    return 'Yes'