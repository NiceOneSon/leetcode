# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        M = mountain_arr
        
        def getMax(prev, prevInd, left, right):
            if left > right:
                return (prev, prevInd)
            
            mid = left + right
            mid //= 2
            
            value = M.get(mid)
            answer = (None, -1)
            if value > prev:
                answer = (value, mid)
                result = getMax(value, mid, mid + 1, right)
            else:
                return (prev, prevInd)
            if not result or (result and result[0] <= answer[0]):
                result = getMax(value, mid, left, mid)
            if result and result[0] > answer[0]:
                answer = result
            return answer
        
        left = 0
        right = M.length()
        answer = getMax(-1, -1, left = left, right = right)
        
        left = 0
        right = answer[1] + 1
        
        while left <= right:
            mid = left + right
            mid //= 2
            value = M.get(mid)
            if value == target:
                return mid
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1
        left = answer[1]
        right = M.length() 
        while left < right:
            mid = left + right
            mid //= 2
            value = M.get(mid)
            if value == target:
                return mid
            elif value < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
                