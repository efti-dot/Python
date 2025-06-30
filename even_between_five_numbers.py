a = input()
b = input()
c = input()
d = input()
e = input()

x = [int(a), int(b), int(c), int(d), int(e)]
count = 0
for i in range(len(x)):
  if x[i] % 2 == 0 :
    count += 1

print(f"{count} valores pares")