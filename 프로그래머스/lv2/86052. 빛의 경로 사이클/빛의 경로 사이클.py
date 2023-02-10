# Four of directions exists
    # Up, Left, Down, Right
import sys
sys.setrecursionlimit(10 ** 6)

dupli = None

def move(grid, y, x, direction, cnt, dy, dx):
    global dupli
    sy, sx = y + dy[direction], x + dx[direction]
    if 0 > sy:
        sy = len(grid) - 1
    elif sy >= len(grid):
        sy = 0
    if 0 > sx:
        sx = len(grid[0]) - 1
    elif sx >= len(grid[0]):
        sx = 0

    if dupli[sy][sx] & (1 << direction):
        return cnt
    dupli[sy][sx] |= (1 << direction)

    if grid[sy][sx] == 'S':
        answer = move(grid, sy, sx, direction, cnt+1, dy, dx)
    elif grid[sy][sx] == 'L':
        answer = move(grid, sy, sx, (direction + 1) % 4, cnt+1, dy, dx)
    else:
        answer = move(grid, sy, sx, (direction - 1 + 4) % 4, cnt+1, dy, dx)
    return answer    

def solution(grid):
    global dupli
    dupli = [[0] * len(grid[0]) for _ in range(len(grid))]
    answer = []
    dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for i in range(4):
                result = move(grid, y, x, i, 0, dy, dx)
                if result:
                    answer.append(result)
    answer.sort()
    return answer