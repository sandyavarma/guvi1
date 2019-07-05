dig=int(input())
a=0
  while dig > 0:
    f=dig%10
    a=a+f*f
    dig=dig//10
    print(a)
