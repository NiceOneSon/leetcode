import heapq

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        q =[]
        answer = []
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
                heapq.heappush(q, num)
        
        while q:
            num = heapq.heappop(q)
            answer.append(num)
        nums[:] = answer
        
        return len(nums)

# from collections import OrderedDict
# class Solution(object):
#     def removeDuplicates(self, nums):
#         nums[:] =  OrderedDict.fromkeys(nums)
#         return len(nums)