import heapq
import sys

input = sys.stdin.readline


def calib(left, right, median):
    # 짝수 개라면 작은 쪽을 선택
    
    if len(left) == len(right):
        return left, right, median
    
    elif len(left) > len(right):
        while len(left) > len(right):
            num = heapq.heappop(left)
            heapq.heappush(right, median)
            median = -num

    elif len(left) + 1 < len(right):
        while len(left) + 1 < len(right):
            num = heapq.heappop(right)
            heapq.heappush(left, -median)
            median = num
    
    return left, right, median


N = int(input())

left, right = [], []

median = None

for _ in range(N):
    num = int(input())

    if median == None:
        median = num
    
    elif median <= num:
        heapq.heappush(right, num)
    
    else:
        heapq.heappush(left, -num)


    left, right, median = calib(left, right, median)

    print(median)
