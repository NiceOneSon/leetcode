class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(len(text1) * len(text2))
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return dp(i + 1, j + 1) + 1
            else:
                return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)
