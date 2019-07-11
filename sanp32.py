a,b=map(int(input().split()))
c=0
for x in range(2,b):
  if(a%x==0 and b%x==0):
    c=x
print(c)
