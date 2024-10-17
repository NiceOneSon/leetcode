class Solution:
    def maximumSwap(self, num: int) -> int:
        snum = str(num)
        lnum = list(snum)
        
        length = len(lnum)
        dp = [length - 1 for i in range(length)]
        
        for curr_idx in range(length-2, -1, -1):
            right_idx = curr_idx + 1
            right_pnt = dp[right_idx]
            curr_pnt = curr_idx
            if lnum[curr_pnt] <= lnum[right_pnt]:
                curr_pnt = right_pnt
            dp[curr_idx] = curr_pnt
        
        for curr_idx in range(length):
            pnt = dp[curr_idx]
            if lnum[curr_idx] < lnum[pnt]:
                lnum[curr_idx], lnum[pnt] = lnum[pnt], lnum[curr_idx]
                break
            
        return int(''.join(lnum))
            
                
            