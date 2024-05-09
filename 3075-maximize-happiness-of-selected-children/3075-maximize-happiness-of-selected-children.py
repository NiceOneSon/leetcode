class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        import heapq
        
        q = []
        
        happiness.sort()
        
        answer = 0
        for count in range(k):
            person = happiness.pop()
            if person - count > 0:
                answer += person - count
        
        return answer