from functools import lru_cache
class Solution:
    @lru_cache(50)
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2) 