def solution(board, skill):
    answer = 0
    
    # skill 정보를 담을 수 있는 행렬을 생성한다.
    ROW, COL = len(board), len(board[0])
    routes = [[0] * (COL+1) for i in range(ROW+1)]
    
    # 스킬에 따라 4 개 꼭지점을 업데이트 한다.
    for types, r1, c1, r2, c2, deg in skill:
        if types == 1:
            deg = -deg
        r2 += 1
        c2 += 1
        # 회복 기준
        routes[r1][c1] += deg
        routes[r1][c2] += -deg
        routes[r2][c1] += -deg
        routes[r2][c2] += deg
    
    # 업데이트 된 행렬을 가지고 Board를 업데이트하고 0이하인 값들을 세 출력한다.
    
    for r in range(ROW):
        val = 0
        for c in range(COL):
            if routes[r][c]:
                # routes 밑에 row에도 채운다. (넘어가면 continue)
                if r + 1 < ROW:
                    routes[r+1][c] += routes[r][c]
                    
                # val에다 routes 값을 업데이트 한다.
                val += routes[r][c]
                
            board[r][c] += val
            if board[r][c] > 0:
                answer += 1
    
    return answer