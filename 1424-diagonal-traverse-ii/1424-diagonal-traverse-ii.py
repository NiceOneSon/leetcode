class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        orders = []
        for y, row in enumerate(nums):
            for x, val in enumerate(row):
                orders.append(((y + x), x, y, val))
        
        orders.sort()
        
        return map(lambda x : x[3], orders)