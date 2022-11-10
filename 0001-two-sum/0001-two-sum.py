class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        
        for ind, num in enumerate(nums):
            tmp = target - num
            if tmp in visited:
                return [visited[tmp], ind]
            visited[num] = ind