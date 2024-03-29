from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        answer = float("inf")
        nums = sorted(set(nums))
        # print(nums)
        for i, val in enumerate(nums):
            e = bisect_left(nums, val + n)
            # print(i, val, e)
            answer = min(answer, n - e + i)
        return answer
    
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         n = len(nums)
#         nums = sorted(set(nums))
#         ans = sys.maxsize

#         for i, s in enumerate(nums):
#             e = s + n - 1
#             idx = bisect_right(nums, e)

        #     ans = min(ans, n - (idx - i))
        # return ans