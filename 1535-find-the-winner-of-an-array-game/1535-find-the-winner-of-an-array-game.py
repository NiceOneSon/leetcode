class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        
        from collections import defaultdict
        d = defaultdict(int)
        base, other = 0, 1
        while other < len(arr) and d[arr[base]] < k and d[arr[other]] < k:
            if arr[base] < arr[other]:
                base = other
            other += 1
            d[arr[base]] += 1
        return arr[base]