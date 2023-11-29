class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            resid = n % 2
            n >>= 1
            cnt += resid
        return cnt
            