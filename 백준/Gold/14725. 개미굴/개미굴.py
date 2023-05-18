from collections import defaultdict

N = int(input())

routes = {}
for _ in range(N):
    num, *hier = input().split(' ')
    cur = routes
    for height in range(int(num)):
        val = hier[height]
        if val not in cur:
            cur[val] = {}
        cur = cur[val]

def dfs(cur, height):
    chk = False
    for key in cur.keys():
        chk = True
    if chk == False:
        return True
    
    for key in sorted(cur.keys()):
        print(f'{"""--"""*height}{key}')
        dfs(cur[key], height+1)

dfs(routes, 0)
