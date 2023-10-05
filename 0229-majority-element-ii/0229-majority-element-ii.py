class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        counter = defaultdict(int)
        limit = len(nums) // 3
        answer = []
        for num in nums:
            if counter[num] == None:
                continue
            
            counter[num] += 1
            if counter[num] > limit:
                answer.append(num)
                counter[num] = None
        
        return answer 