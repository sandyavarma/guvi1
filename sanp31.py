num1=input().split()
num2=input().split()
num3=input().split()
if(num1[0]==num2[0]==num3[0] or num1[1]==num2[1]==num3[1] or (num1[0]==num1[1] and num2[0]==num2[1] and num3[0]==num3[1])):
    print('yes')
else:
    print('no')
