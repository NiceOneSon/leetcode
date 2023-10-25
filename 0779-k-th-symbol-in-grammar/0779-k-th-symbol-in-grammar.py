class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        result = self.kthGrammar(n - 1, (k - 1)//2 + 1)
        isLeft = (k % 2) != 0
        if isLeft:
            return result
        return abs(result - 1)