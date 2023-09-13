from collections import defaultdict

class Solution:
    def check(self, person, answer, ratings):
        maxnum = 1
        # left check
        if person > 0 and ratings[person-1] < ratings[person]:
            maxnum = max(maxnum, answer[person-1] + 1)
        if person < len(ratings) - 1 and ratings[person+1] < ratings[person]:
            maxnum = max(maxnum, answer[person+1] + 1)
        return maxnum
            
    def candy(self, ratings: List[int]) -> int:
        maxrate = -1
        people_per_rate = defaultdict(list)
        answer = [0] * len(ratings)
        
        for person, rate in enumerate(ratings):
            people_per_rate[rate].append(person)
            maxrate = max(rate, maxrate)
        
        for rate in range(maxrate+1):
            for person in people_per_rate[rate]:
                num = self.check(person, answer, ratings)
                answer[person] = num
        return sum(answer)