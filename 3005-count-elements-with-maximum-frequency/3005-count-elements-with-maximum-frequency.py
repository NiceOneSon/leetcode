class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        
        c = Counter(nums)
        
        maximum = 0
        for key, val in c.items():
            maximum = max(maximum, val)
            
        answer =0 
        for key, val in c.items():
            if val == maximum:
                answer += val
        return answer