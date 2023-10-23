class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        import math
        
        return False if math.log(n, 4) % 1 else True