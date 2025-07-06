X = int(input())
count = 0
for i in range(X, X + 12):
    if i % 2 != 0:
        print(i)
        count += 1
    if count == 6:
        break