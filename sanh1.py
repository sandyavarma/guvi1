m1=int(input())
b=list(map(int,input().split()))
ln=[]
for i in b:
    if b.count(i)>1:
        if str(i) not in ln:
            ln.append(str(i))
if len(ln)==0:
    print("unique")
else:
    print(" ".join(ln))
