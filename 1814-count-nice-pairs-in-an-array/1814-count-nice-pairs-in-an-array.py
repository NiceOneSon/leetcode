class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        diff_dict = defaultdict(int)
        for num in nums:
            numString = str(num)
            revNumString = numString[::-1]
            revNum = int(revNumString)
            diff_dict[(num - revNum)] += 1
        
        import math
        answer = 0
        for val in diff_dict.values():
            answer += math.comb(val, 2)
        return answer % (10**9 + 7)
        