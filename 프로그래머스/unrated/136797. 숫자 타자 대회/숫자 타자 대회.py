from collections import deque, defaultdict
def solution(numbers):
    answer = 0
    dial = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (-1, 0, -1)
    ]
    INF = float('inf')
    dy_2, dx_2 = [-1, 1, 0, 0], [0, 0, -1, 1]
    dy_3, dx_3 = [-1, -1, 1, 1], [-1, 1, -1, 1]
    numbers = map(int, numbers)
    
    def get_num(y, x):
        return dial[y][x]
    
    def get_mat():
        result = [[INF] * 10 for i in range(10)]
        for y in range(4):
            for x in range(3):
                q = deque([(y, x, 0)])
                s_num = get_num(y, x)
                result[s_num][s_num] = 1
                if s_num == -1:
                    continue
                while q:
                    yi, xi, c = q.popleft()
                    for i in range(4):
                        sy, sx = yi + dy_2[i], xi + dx_2[i]
                        if 0<=sy<4 and 0<=sx<3:
                            t_num = get_num(sy, sx)
                            if result[s_num][t_num] > c + 2 and t_num != -1:
                                result[s_num][t_num] = c + 2
                                q.append((sy, sx, c + 2))
                        sy, sx = yi + dy_3[i], xi + dx_3[i]
                        if 0<=sy<4 and 0<=sx<3:
                            t_num = get_num(sy, sx)
                            if result[s_num][t_num] > c + 3 and t_num != -1:
                                result[s_num][t_num] = c + 3
                                q.append((sy, sx, c + 3))
                        
        return result
    result = get_mat()
    s_s = defaultdict(lambda : INF)
    s_s[(4, 6)] = 0
    for number in numbers:
        t_s = defaultdict(lambda : INF)
        for (left, right), cost in s_s.items():
            mover, notmover = left, right
            if number != notmover:
                new_left, new_right = min(number, notmover), max(number, notmover)
                t_s[(new_left, new_right)] = min(t_s[(new_left, new_right)], cost + result[mover][number])
            mover, notmover = right, left
            if number != notmover:
                new_left, new_right = min(number, notmover), max(number, notmover)
                t_s[(new_left, new_right)] = min(t_s[(new_left, new_right)], cost + result[mover][number])
        s_s = t_s
    return min(t_s.values())