from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        q = []
        Times = [(end,idx,start) for idx,(start, end) in enumerate(zip(startTime, endTime))]
        Times.sort()
        endtimes = [end for end, _, _ in Times]
        DP = [0] * len(Times)
        DP[0] = profit[Times[0][1]]
        for timeIdx in range(1, len(Times)):
            end, idx, start = Times[timeIdx]
            prevIdx = bisect_right(endtimes, start)
            # print(timeIdx, prevIdx)
            DP[timeIdx] = max(DP[prevIdx-1] + profit[idx], DP[timeIdx-1])

        return DP[-1]