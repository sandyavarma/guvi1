from itertools import combinations
c,d=map(int,input().split())
m=len(str(c))
a=list(combinations(str(c),m-d))
a.sort()
print(*a[0],sep='')
