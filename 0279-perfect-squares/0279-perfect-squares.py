from functools import lru_cache 

class Solution:
    limit = 100    
    @lru_cache(10**4)
    def numSquares(self, n: int) -> int:
        if n < 0:
            return float('inf')
        if n == 0:
            return 0
        # print(n)
        # Solution.limit -= 1
        # if Solution.limit == 0:
        #     return 0
        num = int(n ** 0.5)
        answer = float('inf')
        while num > 0:
            answer = min(answer, self.numSquares(n - num ** 2) + 1)
            num -= 1
        return answer