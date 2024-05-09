class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        import heapq
        
        q = []
        
        for person in happiness:
            heapq.heappush(q, -person)
        
        answer = 0
        for count in range(k):
            minus_person = heapq.heappop(q)
            person = -minus_person
            if person - count > 0:
                answer += person - count
        
        return answer