def solution(n, cores):

    
    # 2 분탐색
    # 통과를 할 수 없는 마지막 초를 구하는 방법
        # mid는 시간을 나타내고 mid안에 통과가 되면 right = mid - 1 통과가 안되면 left = mid 지정
    # left 시간에는 통과를 할 수 없고 + 1초 뒤에는 통과 할 수 있다.
    # 따라서 for문을 돌려 해당 초에서 result가 n일때 core를 구하는 문제
    
    left, right = 0, 50000
    while left < right:
        mid = left + right + 1
        mid //= 2
        result = len(cores)
        for core in cores:
            result += mid // core
        if result >= n:
            right = mid - 1
        else:
            left = mid
    result = len(cores)
    for core, spend in enumerate(cores, start = 1):
        result += left // spend
    for core, spend in enumerate(cores, start = 1):
        if (left + 1) % spend == 0:
            result += 1
        if result == n:
            return core
