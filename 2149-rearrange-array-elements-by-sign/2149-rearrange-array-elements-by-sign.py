from collections import deque
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        plus = deque()
        minus = deque()
        
        for num in nums:
            if num < 0:
                minus.append(num)
            else:
                plus.append(num)
        
        answer = []
        
        for _ in range(len(nums) // 2):
            answer.append(plus.popleft())
            answer.append(minus.popleft())
        
        return answer