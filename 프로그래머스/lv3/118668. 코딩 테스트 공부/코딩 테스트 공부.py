from functools import reduce
def solution(alp, cop, problems):
    # alp, cop을 기준으로 2차원 배열 생성 # row = alp, col = cop
    alpmax, copmax = reduce(lambda x, y : max(x, y[0]), problems, 0), reduce(lambda x, y : max(x, y[1]), problems, 0)
    INF = float('inf')
    routes = [[INF] * (copmax+1) for i in range(alpmax+1)]
    alp = min(alp, alpmax)
    cop = min(cop, copmax)
    # 한 시간씩 공부했을 때 (최악의 경우) 투자해야 하는 시간 세팅
    routes[alp][cop] = 0
    
    # Problems하나씩 빼서 공부했을 때를 업데이트 둘 다 최대 크기까지(만일 세팅된 값보다 크다면 break)
    for r in range(alp, alpmax+1):
        for c in range(cop, copmax+1):
            if r + 1 <= alpmax:
                routes[r+1][c] = min(routes[r+1][c], routes[r][c] + 1)
            if c + 1 <= copmax:
                routes[r][c+1] = min(routes[r][c+1], routes[r][c] + 1)
            for abil_alp, abil_cop, exp_r, exp_c, cost in problems:
                if r >= abil_alp and c >= abil_cop:
                    newr = (r + exp_r) if r + exp_r < alpmax else alpmax
                    newc = (c + exp_c) if c + exp_c < copmax else copmax
                    routes[newr][newc] = min(routes[newr][newc], routes[r][c] + cost)
    answer = routes[-1][-1]
    return answer