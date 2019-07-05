monday = input()
print(''.join([monday[x:x+2][::-1] for x in range(0, len(monday), 2) ]))
