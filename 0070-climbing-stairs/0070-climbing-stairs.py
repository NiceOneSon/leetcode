from functools import lru_cache
class Solution:
    @lru_cache(50)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        
        return self.climbStairs(n-1) + self.climbStairs(n-2) 