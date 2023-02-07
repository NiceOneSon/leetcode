import sys
sys.setrecursionlimit(1000000)

def union_find(parent, room):
    if room not in parent:
        parent[room] = room + 1
        return room
    else:
        parent[room] = union_find(parent, parent[room])
        return parent[room]

def solution(k, room_number):
    parent = {}
    answer = []
    for room in room_number:
        answer.append(union_find(parent, room))
    return answer