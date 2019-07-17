a1=int(input())
b2=[]
for i in range(a1):
  b2.append(input())
  x1,y2,flag ='',0,False
for m in a2[0]:
  for n in b2[1:]:
    if len(n)==y2:
      flag=True
      break
    if n[y2]!=m:
      break
  else:
    x1+=m
  if flag:
      break
  y2+=1
print(x1)
