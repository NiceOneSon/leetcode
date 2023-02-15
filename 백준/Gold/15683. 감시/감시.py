import sys
import copy
from collections import deque
input = sys.stdin.readline

limit = 100
dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)
direction = (
        (),
        ((0,), (1,), (2,), (3,)),
        ((0, 2), (1, 3)),
        ((0, 1), (1, 2), (2, 3), (3, 0)),
        ((0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)),
        ((0, 1, 2, 3), )
    )
Y, X = map(int, input().split(' '))
answer = X * Y

def move(y, x, i, visited, routes):
    cnt = 0
    while 0<=y+dy[i]<Y and 0<=x+dx[i]<X and routes[y+dy[i]][x+dx[i]] != '6':
        y = y+dy[i]
        x = x+dx[i]
        if not visited[y][x]:
            cnt += 1
            visited[y][x] = True
    return visited, cnt

def dfs(nums_list, nums_list_ind, visited, routes):
    global answer

    if nums_list_ind == len(nums_list):
        cnt = 0
        for y in range(Y):
            for x in range(X):
                if visited[y][x]:
                    continue
                if routes[y][x] != '0':
                    continue
                cnt += 1
        return cnt
    
    y, x, num = nums_list[nums_list_ind]
    directions = direction[num]
    for indexes in directions: # indexes (0, 1, 2)
        tmpvisited = copy.deepcopy(visited)
        total = 0
        for index in indexes:
            tmpvisited, tmpcnt = move(y, x, index, tmpvisited, routes)
            total += tmpcnt
        result = dfs(nums_list, nums_list_ind+1, tmpvisited, routes)
        if answer > result:
            answer = result
            # if result == 6:
            #     print(' ')
            #     [print(row) for row in tmpvisited]
    return answer
                

if __name__ == '__main__':
    routes = []
    nums_list = []
    zeros = 0
    for i in range(Y):
        routes.append(list(input()[:-1].split(' ')))
        for val in routes[-1]:
            if val == '0':
                zeros += 1

    for y in range(Y):
        for x in range(X):
            if routes[y][x] not in ('0', '6'):
                nums_list.append((y, x, int(routes[y][x])))
    
    visited = [[False] * X for i in range(Y)]
    print(dfs(nums_list, 0, visited, routes))