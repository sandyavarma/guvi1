m,n =map(list,input().spilt())
cou=0
if(len(m)==len(n))
  for i in range(0,len(m)):
    if(m[i]==n[i]):
      continue
    else:
      cou=cou+1
if(cou==1):
  print("yes")
else:
  print("no")
