class Solution:
    def maximumSwap(self, num: int) -> int:
        snum = str(num)
        lnum = list(snum)
        
        length = len(lnum)
        dp = [length - 1 for i in range(length)]
        
        for curr_idx in range(length-2, -1, -1):
            right_idx = curr_idx + 1
            left_pnt = curr_idx
            right_pnt = dp[right_idx]
            
            pnt = curr_idx
            if lnum[left_pnt] <= lnum[right_pnt]:
                pnt = right_pnt
                
            dp[curr_idx] = pnt
        
        for curr_idx in range(length):
            pnt = dp[curr_idx]
            if lnum[curr_idx] < lnum[pnt]:
                lnum[curr_idx], lnum[pnt] = lnum[pnt], lnum[curr_idx]
                break
            
        return int(''.join(lnum))
            
                
            