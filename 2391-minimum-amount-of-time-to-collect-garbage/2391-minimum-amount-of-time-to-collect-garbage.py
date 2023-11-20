class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def getTimeDelta(house, nexthouse):
            timeDelta = 0
            for ind in range(house, nexthouse):
                timeDelta += travel[ind]
            return timeDelta
        
        garbageList = 'MPG'
        answer = 0
        for garbageString in garbageList:
            stack = []
            for house in range(len(garbage)-1, -1, -1):
                if garbageString in garbage[house]:
                    stack.append((garbage[house].count(garbageString), house))
            if not stack:
                continue
            if stack[-1][1] != 0:
                stack.append((garbage[0].count(garbageString), 0))
            # print(stack)
            while stack:
                gettingTime, house = stack.pop()
                answer += gettingTime
                if stack:
                    nexthouse = stack[-1][-1]
                    timeDelta = getTimeDelta(house, nexthouse)
                    answer += timeDelta
            # print(answer, garbageString)
        return answer