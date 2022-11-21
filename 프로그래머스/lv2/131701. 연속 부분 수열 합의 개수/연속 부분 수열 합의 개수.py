# def solution(elements):
#     answer = 0
#     DP = [elements[:] for i in range(len(elements))]
#     s = set(elements)
#     for ind in range(1, len(elements)):
#         for pointer in range(len(elements)):
#             DP[ind][pointer] = DP[ind-1][pointer] + elements[(pointer + ind) % len(elements)]
#             s.add(DP[ind][pointer])
#     # print(DP)
#     return len(s)
def solution(elements):
    answer = 0
    l = set()

    n = len(elements)

    add = [0 for i in range(n)]

    for i in range(n):
        add = [add[j] + elements[(i+j)%n] for j in range(n)]

        for a in add:
            l.add(a)

    return len(l)