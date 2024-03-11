class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        answer = []
        for alphabet in order:
            answer += [alphabet] * c[alphabet]
        order = set(order)
        for alphabet in s:
            if alphabet not in order:
                answer.append(alphabet)
                
        return ''.join(answer)