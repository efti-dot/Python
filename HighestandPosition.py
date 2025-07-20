a = []
for i in range(1,6):
    a.append(int(input()))

highest = max(a)
print(highest)
index = a.index(highest)
print(index+1)