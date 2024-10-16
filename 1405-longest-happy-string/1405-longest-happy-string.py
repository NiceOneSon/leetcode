import heapq
class Solution:
    
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        s = []
        heapq.heappush(q, (-a, 'a'))
        heapq.heappush(q, (-b, 'b'))
        heapq.heappush(q, (-c, 'c'))
        
        while q:
            n, alphabet = heapq.heappop(q)
            if len(s) >= 2 and alphabet == s[-1] and alphabet == s[-2]:
                if not q:
                    continue
                _n, _alphabet = heapq.heappop(q)
                heapq.heappush(q, (n, alphabet))
                n, alphabet = _n, _alphabet
            if n == 0:
                continue
            s.append(alphabet)
            heapq.heappush(q, (n+1, alphabet))

        return ''.join(s)