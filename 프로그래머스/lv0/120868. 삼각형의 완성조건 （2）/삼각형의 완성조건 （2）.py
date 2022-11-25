def solution(sides):
    s = set()
    
    minx, maxx = min(sides), max(sides)
    num = maxx
    # 긴변이 side 내 max일 때
    while True:
        if maxx > minx + num:
            break
        if maxx > num:
            s.add(num)
        num -= 1
    num = maxx
    while sum(sides) > num:
        # print(1)
        s.add(num)
        num += 1
    
    return len(s) -1