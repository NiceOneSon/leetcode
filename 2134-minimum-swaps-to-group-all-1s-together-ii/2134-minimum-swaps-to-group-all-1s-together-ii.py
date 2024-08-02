class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window_size: int = nums.count(1)
        num_length: int = len(nums)
        if window_size == 0:
            return 0
        if window_size == num_length:
            return 0
        answer: int = num_length
        curr_cnt: int = nums[:window_size].count(1)
        
        for idx_left in range(num_length):
            idx_right: int = (idx_left + window_size) % num_length
            if nums[idx_left] == 1:
                curr_cnt -= 1
            if nums[idx_right] == 1:
                curr_cnt += 1
            answer = min(answer, window_size - curr_cnt) # this is 1 counts in the window 
        return answer