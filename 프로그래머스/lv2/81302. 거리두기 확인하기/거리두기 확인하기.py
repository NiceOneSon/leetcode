from collections import deque

def check(routes):
    persons = []
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    visited = [[False] * 5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            if routes[y][x] == 'P':
                persons.append((y, x))
    
    for person in persons:
        q = deque()
        y, x = person
        q.append((y, x, 0))
        visited[y][x] = True
        while q:
            y, x, cnt = q.popleft()
            for i in range(4):
                sy, sx = y+dy[i], x+dx[i]
                if not(0<=sy<5 and 0<=sx<5):
                    continue
                if visited[sy][sx]:
                    continue
                if routes[sy][sx] == 'P':
                    return False
                if routes[sy][sx] == 'X':
                    continue
                
                visited[sy][sx] = True
                if cnt == 1:
                    continue
                q.append((sy, sx, cnt+1))
    return True
                
            
    

def solution(places):
    answer = []
    for place in places:
        result = check(place)
        answer.append(int(result))
    return answer