def InACircle(r):
    R_squared = r ** 2
    result = r * 4 + 1
    surfaced = 4
    for i in range(1, r):
        other_r_squared = R_squared - (i ** 2)
        tmp = other_r_squared ** 0.5
        other_r = int(tmp)
        if tmp == other_r:
            surfaced += 4
        result += (other_r * 4)
    return result, surfaced

def solution(r1, r2):
    answer = 0
    r2_result, _ = InACircle(r2)
    r1_result, r1_surface = InACircle(r1)
    
    return r2_result - r1_result + r1_surface