from collections import deque, defaultdict

dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

def check(y, x, i, board):
    for j in range(2):
        if i == 0:
            sy = y - 1
            sx = x + j
        elif i == 1:
            sy = y + 1
            sx = x + j
        elif i == 2:
            sx = x - 1
            sy = y + j
        else:
            sx = x + 1
            sy = y + j
        if not 0<=sy<len(board) or not 0<=sx<len(board):
            return False
        if board[sy][sx]:
            return False
    return True
    
def rotate(q, wing1, wing2, sec, board, dupli):
    global cnt
    # 1. 가로 방향 1 체크
    y1, x1 = wing1 #upper
    y2, x2 = wing2
    vertical = True if y1 == y2 else False
    for i in range(4): # [좌, 우]
        if not check(y1, x1, i, board):
            continue
        if i == 0 and vertical:
            sy, sx = y1 - 1, x1
            if dupli[((sy, sx), (y1, x1))] < sec + 1:
                pass
            else:
                dupli[((sy, sx), (y1, x1))] = sec + 1
                q.append(((sy, sx), (y1, x1), sec + 1))
            sy, sx = y2 - 1, x2
            if dupli[((sy, sx), (y2, x2))] < sec + 1:
                pass
            else:
                dupli[((sy, sx), (y2, x2))] = sec + 1
                q.append(((sy, sx), (y2, x2), sec + 1))
        elif i == 1 and vertical:
            sy, sx = y2 + 1, x2
            if dupli[((y2, x2), (sy, sx))] < sec + 1:
                pass
            else:
                dupli[((y2, x2), (sy, sx))] = sec + 1
                q.append(((y2, x2), (sy, sx), sec + 1))
            sy, sx = y1 + 1, x1
            if dupli[((y1, x1), (sy, sx))] < sec + 1:
                pass
            else:
                dupli[((y1, x1), (sy, sx))] = sec + 1
                q.append(((y1, x1), (sy, sx), sec + 1))
            
        elif i == 2 and not vertical:
            sy, sx = y2, x2 - 1
            if dupli[((sy, sx), (y2, x2))] < sec + 1:
                pass
            else:
                dupli[((sy, sx), (y2, x2))] = sec + 1
                q.append(((sy, sx), (y2, x2), sec + 1))
            sy, sx = y1, x1 - 1
            if dupli[((sy, sx), (y1, x1))] < sec + 1:
                pass
            else:
                dupli[((sy, sx), (y1, x1))] = sec + 1
                q.append(((sy, sx), (y1, x1), sec + 1))
        elif i == 3 and not vertical:
            sy, sx = y2, x2 + 1
            if dupli[((y2, x2), (sy, sx))] < sec + 1:
                pass
            else:
                dupli[((y2, x2), (sy, sx))] = sec + 1
                q.append(((y2, x2), (sy, sx), sec + 1))
            
            sy, sx = y1, x1 + 1
            if dupli[((y1, x1), (sy, sx))] < sec + 1:
                pass
            else:
                dupli[((y1, x1), (sy, sx))] = sec + 1
                q.append(((y1, x1), (sy, sx), sec + 1))
            
            

def solution(board):
    INF = float('inf')
    answer = INF
    target = (len(board)-1, len(board)-1)
    q = deque([((0, 0), (0, 1), 0)])
    dupli = defaultdict(lambda : INF)
    dupli[((0,0), (0,1))] = 0
    
    while q:
        lwing, rwing, sec = q.popleft()
        lwing, rwing = sorted([lwing, rwing])
        if sec >= answer:
            continue
        if lwing == target or rwing == target:
            answer = min(answer, sec)
            continue
        
        for i in range(4):
            sly, slx = lwing[0] + dy[i], lwing[1] + dx[i]
            sry, srx = rwing[0] + dy[i], rwing[1] + dx[i]
            if not 0<=sly<len(board) or not 0<=sry<len(board):
                continue
            if not 0<=slx<len(board) or not 0<=srx<len(board):
                continue
            if board[sly][slx] or board[sry][srx]:
                continue
            if dupli[((sly, slx), (sry, srx))] <= sec + 1:
                continue
            dupli[((sly, slx), (sry, srx))] = sec + 1
            q.append(((sly, slx), (sry, srx), sec + 1))
        
        rotate(q, lwing, rwing, sec, board, dupli)
        
    return answer