import heapq
from collections import defaultdict

class Solution:
    def minDeletions(self, string: str) -> int:
        s = set()
        q = []
        alphabet = defaultdict(int)
        answer = 0
        
        for alpha in string:
            alphabet[alpha] += 1
        
        for key, val in alphabet.items():
            heapq.heappush(q, (-val, key))
        
        while q:
            value, alphabet = heapq.heappop(q)
            if value not in s:
                s.add(value)
            else:
                value += 1
                answer += 1
                if value not in s:
                    s.add(value)
                    continue
                if value < 0:
                    heapq.heappush(q, (value, alphabet))
                
        
        return answer