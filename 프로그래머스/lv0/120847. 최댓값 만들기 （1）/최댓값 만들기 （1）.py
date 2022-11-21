def solution(numbers):
    one, two = 0, 0
    for num in numbers:
        if one < num:
            two = one
            one = num
        elif two < num:
            two = num
    return one * two