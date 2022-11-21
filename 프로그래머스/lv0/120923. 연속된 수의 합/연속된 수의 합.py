def solution(num, total):
    base = -100
    added = [i for i in range(num)]
    
    while base * num + sum(added) < total:
        base += 1
        
    return [n + base for n in added]