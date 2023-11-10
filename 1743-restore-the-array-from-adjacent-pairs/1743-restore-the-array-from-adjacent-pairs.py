class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        from collections import defaultdict
        d_cnt = defaultdict(list)
        for a, b in adjacentPairs:
            d_cnt[a].append(b)
            d_cnt[b].append(a)
        dupli = set()
        answer = []
        for number, adj in d_cnt.items():
            if len(adj) == 1:
                answer.append(number)
                dupli.add(number)
                break
        
        for _ in range(len(adjacentPairs)):
            for number in d_cnt[answer[-1]]:
                if number in dupli: continue
                answer.append(number)
                dupli.add(number)
        return answer