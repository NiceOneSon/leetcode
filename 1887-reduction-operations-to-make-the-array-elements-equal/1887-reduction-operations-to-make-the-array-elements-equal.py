from collections import defaultdict

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        q = []
        nums_count_dict = defaultdict(int)
        
        for num in nums:
            nums_count_dict[num] += 1
        
        nums_set_list = sorted(set([num for num in nums_count_dict.keys()]))
        
        nums_index_dict = {}
        
        for index, num in enumerate(nums_set_list):
            nums_index_dict[num] = index
        
        answer = 0
        
        for key, val in nums_count_dict.items():
            answer += nums_index_dict[key] * val
        
        return answer