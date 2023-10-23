class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        return True if n > 0 and math.log(n, 4).is_integer() else False