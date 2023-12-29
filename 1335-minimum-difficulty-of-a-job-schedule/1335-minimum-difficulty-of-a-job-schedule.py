from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], remain: int) -> int:
        INF = float('inf')
        
        if remain > len(jobDifficulty):
            return -1
        
        DP = [[0] * (len(jobDifficulty)) for _ in range(len(jobDifficulty))]
        for i in range(len(jobDifficulty)):
            maxval = jobDifficulty[i]
            DP[i][i] = maxval
            for j in range(i, len(jobDifficulty)):
                maxval = max(maxval, jobDifficulty[j])
                DP[i][j] = maxval
            
        # print(DP)
        @lru_cache(len(jobDifficulty) ** 2 * remain)
        def recursive(left: int, right: int, d: int):
            if d == 0:
                if right == len(jobDifficulty):
                    if right == left:
                        return 0
                    return DP[left][right-1]
                else:
                    return INF
            
            if right >= len(jobDifficulty):
                return INF
            
            answer = INF
            answer = min(answer, recursive(left, right + 1, d))
            answer = min(answer, recursive(right+1, right+1, d - 1) + DP[left][right])
            
            return answer
        return recursive(0, 0, remain)
