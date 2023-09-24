from functools import lru_cache

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        @lru_cache
        def recur(y, x):
            if y == 1 and x == 1:
                return max(poured - 1, 0)
            
            answer = 0
            if y - 1 >= x:
                answer += recur(y-1, x) / 2
            if x - 1 >= 1:
                answer += recur(y-1, x-1) / 2
            return max(answer - 1, 0)
        
        answer = 0
        y, x = query_row + 1, query_glass + 1
        if y == 1 and x == 1:
            return int(bool(poured))
            
        if y - 1 >= x:
            answer += recur(y-1, x) / 2
        if x - 1 >= 1:
            answer += recur(y-1, x-1) / 2
        return min(answer, 1)