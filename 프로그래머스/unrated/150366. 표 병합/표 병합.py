
def solution(commands):

    answer = []
    parents = [[(i, j) for j in range(51)] for i in range(51)]
    cats = [[''] * 51 for i in range(51)]

    def find(y, x):
        if (y, x) != parents[y][x]:
            return find(*parents[y][x])
        return parents[y][x]

    def union(y1, x1, y2, x2):
        py1, px1 = find(y1, x1)
        py2, px2 = find(y2, x2)
        if cats[py1][px1]:
            for i in range(51):
                for j in range(51):
                    # if (1, 1, 4, 4) == (y1, x1, y2, x2) and (i, j) == (4, 4):
                    #     print(i, j, find(i, j), (py2, px2))
                    if find(i, j) == (py2, px2) and (i, j) != (py2, px2):
                        parents[i][j] = (py1, px1)
                        cats[i][j] = cats[py1][px1]
            else:
                parents[py2][px2] = (py1, px1)
                cats[py2][px2] = cats[py1][px1]

        else:
            for i in range(51):
                for j in range(51):
                    if find(i, j) == (py1, px1) and (i, j) != (py1, px1):
                        parents[i][j] = (py2, px2)
                        cats[i][j] = cats[py2][px2]
            else:
                parents[py1][px1] = (py2, px2)
                cats[py1][px1] = cats[py2][px2]

            
    for command in commands:
        act, *etc = command.split(' ')
        if act == 'UPDATE':
            if len(etc) == 3:
                y, x, cat = etc
                y, x = int(y), int(x)
                py, px = find(y, x)
                for i in range(51):
                    for j in range(51):
                        if find(i, j) == (py, px):
                            cats[i][j] = cat
            else:
                val, cat = etc
                for i in range(51):
                    for j in range(51):
                        if cats[i][j] == val:
                            cats[i][j] = cat

        elif act == 'MERGE':
            y1, x1, y2, x2 = map(int, etc)
            union(y1, x1, y2, x2)
        
        elif act == 'UNMERGE':
            y, x = etc
            y, x = int(y), int(x)
            py, px = find(y, x)
            cat = cats[py][px]
            for i in range(51):
                for j in range(51):
                    if (py, px) == find(i, j):
                        parents[i][j] = (i, j)
                        cats[i][j] = ''
            cats[y][x] = cat
        
        else:
            y, x = etc
            y, x = int(y), int(x)
            py, px = find(y, x)
            answer.append((cats[py][px] if cats[py][px] else 'EMPTY'))


    return answer