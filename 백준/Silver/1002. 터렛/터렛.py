N = int(input())

for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(' '))
    
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    # 동심원
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif dist < r1 or dist < r2:
        if r1 == r2:
            print(2)
        elif r1 > r2:
            if dist + r2 < r1:
                print(0)
            elif dist + r2 == r1:
                print(1)
            else:
                print(2)
        elif r1 < r2:
            if dist + r1 < r2:
                print(0)
            elif dist + r1 == r2:
                print(1)
            else:
                print(2)
    elif dist > r1+r2:
        print(0)
    elif dist == r1+r2:
        print(1)
    else:
        print(2)

    

    