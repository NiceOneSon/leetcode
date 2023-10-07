MOD = 10 ** 9 + 7

class Solution:
    def numOfArrays(self, n0: int, m0: int, k0: int) -> int:
        
        @lru_cache(None)
        def recurse(n,m,k):
            if n == n0:
                return k == k0
            
            # keep m same
            ret = m * recurse(n+1,m,k)
            
            # raise m
            for j in range(m+1,m0+1):
                ret += recurse(n+1, j, k+1)
            
            return ret % MOD
        
        return recurse(0,0,0)