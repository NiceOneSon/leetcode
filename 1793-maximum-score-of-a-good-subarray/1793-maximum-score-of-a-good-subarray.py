class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left, right = k, k
        result = nums[k]
        minNum = nums[k]
        answer = nums[k]
        def move(isLeft, result, minNum, left, right):
            if isLeft:
                return min(minNum, nums[left - 1]) * (right + 2 - left), min(minNum, nums[left - 1])
            else:
                return min(minNum, nums[right + 1]) * (right + 2 - left), min(minNum, nums[right + 1])
            
        while left > 0 and right < len(nums) - 1:
            goLeft, leftMinNum = move(True, result, minNum, left, right)
            goRight, rightMinNum = move(False, result, minNum, left, right)
            if goRight > goLeft:
                answer = max(answer, goRight)
                minNum = rightMinNum
                right += 1
                # print(left, right, answer)
            else:
                answer = max(answer, goLeft)
                minNum = leftMinNum
                left -= 1
                # print(left, right, answer)
        else:
            if left == 0:
                while right < len(nums) - 1:
                    goRight, rightMinNum = move(False, result, minNum, left, right)
                    answer = max(answer, goRight)
                    minNum = rightMinNum
                    right += 1
                    # print(left, right, answer)
            else:
                while left > 0:
                    goLeft, leftMinNum = move(True, result, minNum, left, right)
                    answer = max(answer, goLeft)
                    minNum = leftMinNum
                    left -= 1
                    # print(left, right, answer)
        return answer
            