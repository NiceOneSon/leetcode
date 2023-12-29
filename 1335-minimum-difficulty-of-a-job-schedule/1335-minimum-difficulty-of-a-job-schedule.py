from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], remain: int) -> int:
        INF = float('inf')
        
        if remain > len(jobDifficulty):
            return -1
        length = len(jobDifficulty)
        @lru_cache(length ** 2)
        def recursive(left: int, right: int, d: int, maxval: int):
            if d == 0:
                if right == len(jobDifficulty):
                    return maxval if maxval else 0
                else:
                    return INF
            
            if right >= len(jobDifficulty):
                return INF
            
            if maxval == None:
                maxval = jobDifficulty[left]
            
            answer = INF
            answer = min(answer, recursive(left, right + 1, d, max(maxval, jobDifficulty[right])))
            answer = min(answer, recursive(right+1, right+1, d - 1, None) + max(maxval, jobDifficulty[right]))
            
            return answer
        
        return recursive(0, 0, remain, None)
        
                        