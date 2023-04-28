# DP
# TC : 150 * 150 * 100

def solution(alp, cop, problems):
    # init
    INF = float('inf')
    answer = INF
    row, col = 151, 151
    DP = [[INF] * col for _ in range(row)]
    
    for y in range(row):
        for x in range(col):
            if y < alp and x < cop:
                DP[y][x] = 0
            elif y < alp and x >= cop:
                DP[y][x] = x - cop
            elif y >= alp and x < cop:
                DP[y][x] = y - alp
            else:
                DP[y][x] = y - alp +  x - cop
    
    maxal, maxco = 0, 0
    for al, co, _, _, _ in problems:
        maxal = max(maxal, al)
        maxco = max(maxco, co)
    
    for y in range(alp, row):
        for x in range(cop, col):
            for lalp, lcop, add_al, add_co, cost in problems:
                if y >= lalp and x >=lcop:
                    sy, sx = y+add_al, x+add_co
                    sy, sx = min(sy, row-1), min(sx, col-1)
                    DP[sy][sx] = min(DP[sy][sx], DP[y][x] + cost)
    
    for y in range(row):
        for x in range(col):
            if y >= maxal and x >= maxco:
                if answer > DP[y][x]:
                    answer = DP[y][x]
    
    return answer
            