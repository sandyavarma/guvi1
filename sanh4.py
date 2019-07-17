N=int(input())
P1=input(" ")
P1=list(P1.split(' '))
c={}
for i in P1:
   if i in c:
      c[i]+=1
   else:
      c[i]=1
for key,value in c.items():
  if value==1:
     print(key)
