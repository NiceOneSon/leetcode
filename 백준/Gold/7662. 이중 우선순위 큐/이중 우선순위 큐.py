import sys,heapq
for _ in range(int(sys.stdin.readline())):
    l=[]
    maxl=[]
    d={}
    for _ in range(int(sys.stdin.readline())):
        i,j=sys.stdin.readline().split()
        if i=='I':
            j=int(j)
            heapq.heappush(l,j)
            heapq.heappush(maxl,-j)
            if j in d:
                d[j]+=1
            else:
                d[j]=1
        elif j=='-1':
            try:
                while True:
                    t=heapq.heappop(l)
                    if d[t]:
                        d[t]-=1
                        break
            except:
                continue
        else:
            try:
                while True:
                    t=heapq.heappop(maxl)
                    if d[-t]:
                        d[-t]-=1
                        break
            except:
                continue
    t=d.copy()
    for i in t:
        if d[i]==0:
            del d[i]
    if d:
        print(max(d),min(d))
    else:
        print('EMPTY')