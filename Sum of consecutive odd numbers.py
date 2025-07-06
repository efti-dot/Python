X = int(input())
Y = int(input())
sum = 0
s = min(X, Y) + 1
e= max(X, Y)
for i in range(s, e):
    if i % 2 != 0:
        sum += i

print(sum)