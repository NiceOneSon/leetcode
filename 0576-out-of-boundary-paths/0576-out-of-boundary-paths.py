from collections import deque
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
        q = deque()
        q.append((startRow, startColumn, 1))
        def simulation(q):
            tmpq, score = deque(), 0
            while q:
                y, x, cnt = q.popleft()
                for i in range(4):
                    sy, sx = y+dy[i], x+dx[i]
                    if not(0<=sy<m) or not(0<=sx<n):
                        score += cnt
                        continue
                    tmpq.append((sy, sx, cnt))
            return tmpq, score
        
        def compression(q):
            list_cnt = defaultdict(int)
            while q:
                y, x, cnt = q.popleft()
                list_cnt[(y, x)] += cnt
            tmpq = deque()
            for (y, x), cnt in list_cnt.items():
                tmpq.append((y, x, cnt))
            return tmpq
        
        answer = 0
        for i in range(maxMove):
            q, score = simulation(q)
            q = compression(q)
            answer += score
        MOD=(10**9 + 7)
        return answer % MOD
# 1
# 3
# 3
# 0
# 1