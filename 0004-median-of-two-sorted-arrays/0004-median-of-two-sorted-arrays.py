from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        answer = nums1 + nums2
        answer.sort()
        
        if len(answer) % 2:
            return answer[len(answer)//2]
        else:
            return (answer[len(answer)//2] + answer[len(answer)//2 - 1]) / 2
            
        