import sys
sys.setrecursionlimit(10**6)

def solution(s):
    answer = 0
    def recur(start, ind, cnt, answer):
        if ind >= len(s) or start >= len(s):
            return answer + (1 if start < len(s) else 0)
        
        if s[start] == s[ind]:
            cnt += 1
        else:
            cnt -= 1
        
        if cnt == 0:
            return recur(ind + 1, ind + 2, 1, answer + 1)
        else:
            return recur(start, ind + 1, cnt, answer)
    return recur(0, 1, 1, 0)