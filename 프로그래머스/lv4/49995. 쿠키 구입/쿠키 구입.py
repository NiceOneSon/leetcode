# from itertools import accumulate

# def solution(cookie):
#     answer = 0
#     for m in range(len(cookie)-1):
#         a = set()
#         b = set()
#         tmp = 0
#         for ind in range(m, -1, -1):
#             tmp += cookie[ind]
#             a.add(tmp)
#         tmp = 0
#         for ind in range(m+1, len(cookie)):
#             tmp += cookie[ind]
#             b.add(tmp)
        
#         c = a & b
#         # print(m, c, f'a : {a}, b : {b}')
#         if c:
#             answer = max(*c, answer)
#     return answer
from itertools import accumulate

def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b

        if c:
            answer = max(*c, answer)
    return answer