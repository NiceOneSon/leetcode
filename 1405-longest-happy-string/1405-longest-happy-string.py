import heapq
class Solution:
    
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        s = []
        heapq.heappush(q, (-a, 1))
        heapq.heappush(q, (-b, 2))
        heapq.heappush(q, (-c, 3))
        
        while q:
            n, pnt = heapq.heappop(q)
            
            if len(s) >= 2 and pnt == s[-1] and pnt == s[-2]:
                if q:
                    _n, _pnt = heapq.heappop(q)
                    heapq.heappush(q, (n, pnt))
                    n, pnt = _n, _pnt
                if not q:
                    continue
            if n >= 0:
                continue
            s.append(pnt)
            heapq.heappush(q, (n+1, pnt))
            
            
        for idx in range(len(s)):
            if s[idx] == 1:
                s[idx] = 'a'
            elif s[idx] == 2:
                s[idx] = 'b'
            else:
                s[idx] = 'c'

        return ''.join(s)