from collections import defaultdict
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        length = reduce(lambda x, y: max(x, y[1]), flowers, 0) + 1
        plus_minus = defaultdict(int)
        
        flower = 0
        index = 0
        answer = []
        for s, e in flowers:
            plus_minus[s] += 1
            plus_minus[e + 1] -= 1
        hash = {}
        
        hashinfo = sorted([(key,val) for key, val in plus_minus.items()])
        
        stack = [(0, 0)]
        for key, val in hashinfo:
            if val > 0:
                stack.append((key, stack[-1][1] + val))
            else:
                stack.append((key, stack[-1][1] + val))
        refer = [key for key, _ in stack]
        from bisect import bisect_left
        answer = []
        # print(stack)
        for person in people:
            ind = bisect_left(refer, person)
            if ind >= len(refer):
                answer.append(0)
            elif stack[ind][0] > person:
                answer.append(stack[ind-1][1])
            else:
                answer.append(stack[ind][1])
        return answer
                