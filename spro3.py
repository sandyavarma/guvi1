p,q=input().split()
o=abs(len(q)-len(p))
for i in range(len(p)):
    if(len(q)==1 and q[i] in p):
        break
    if(p[i]!=q[i]):
        o=o+1
print(o)
