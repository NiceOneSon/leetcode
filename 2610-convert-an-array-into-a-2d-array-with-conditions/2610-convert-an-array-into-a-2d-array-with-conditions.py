from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        distributor = defaultdict(int)
        answer = []
        for num in nums:
            if len(answer) <= distributor[num]:
                answer.append([num])
            else:
                ind = distributor[num]
                
                answer[ind].append(num)
            
            distributor[num] += 1
        return answer