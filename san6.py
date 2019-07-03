import calendar
year = int(input())
if calendar.isleap(year) == True:
  print('Yes')
else:
  print('No')
