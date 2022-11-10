from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = [(''.join(sorted(s)), s) for s in strs]
        strs.sort()
        answer = []
        prev = False
        for srted, s in strs:
            if prev != srted:
                prev = srted
                answer.append([s])
            else:
                answer[-1].append(s)
        return answer