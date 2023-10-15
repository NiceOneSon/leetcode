class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        from functools import lru_cache
        
        @lru_cache(None)
        def recursive(pos, opp) -> int:
            if opp == 0:
                if pos == 0:
                    return 1
                return 0
            if pos < 0 or pos >= arrLen:
                return 0
            return recursive(pos, opp - 1) + recursive(pos + 1, opp - 1) + recursive(pos - 1, opp - 1)
        return recursive(0, steps) % (10**9 + 7)
            